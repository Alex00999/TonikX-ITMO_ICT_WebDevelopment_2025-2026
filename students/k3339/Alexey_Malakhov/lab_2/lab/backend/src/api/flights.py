from fastapi import APIRouter, Depends, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session
from src.models.flight import Flight

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import selectinload

templates = Jinja2Templates(directory="src/templates")
router = APIRouter(prefix="/flights")


@router.get("/detail/{flight_id}", response_class=HTMLResponse)
async def flight_by_id(flight_id: int, request: Request, session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(Flight).where(Flight.id_flight == flight_id).options(selectinload(Flight.users))
    )
    return templates.TemplateResponse(
        "flight/flight_detailed.html", {"request": request, "flight": result.scalars().first()}
    )


@router.get("", response_class=HTMLResponse)
async def flights(request: Request, session: AsyncSession = Depends(get_session), type: str | None = None):
    query = select(Flight)

    if type == "departures":
        query = query.filter(Flight.flight_type_id == 2)
    elif type == "arrivals":
        query = query.filter(Flight.flight_type_id == 1)

    result = await session.execute(query)
    flights = result.scalars().all()

    return templates.TemplateResponse(
        "flight/flights.html",
        {"request": request, "flights": flights, "filter_type": type or "all"},
    )


@router.get("/edit/{flight_id}", response_class=HTMLResponse)
async def edit_flight(flight_id: int, request: Request, session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(Flight).where(Flight.id_flight == flight_id).options(selectinload(Flight.users))
    )
    return templates.TemplateResponse(
        "flight/flight_edit.html", {"request": request, "flight": result.scalars().first()}
    )


@router.post("/edit/{flight_id}")
async def edit_flight_submit(flight_id: int, request: Request, session: AsyncSession = Depends(get_session)):
    form = await request.form()
    flight = await session.get(Flight, flight_id)
    if not flight:
        return RedirectResponse("/flights", status_code=303)

    flight.brand = (form.get("brand") or "").strip()  # type: ignore
    flight.model = (form.get("model") or "").strip()  # type: ignore
    flight.plate = (form.get("plate") or "").strip()  # type: ignore
    flight.color = (form.get("color") or "").strip()  # type: ignore

    try:
        await session.commit()
    except Exception:
        await session.rollback()
        return RedirectResponse(f"/flights/edit/{flight_id}", status_code=303)

    return RedirectResponse(f"/flights/edit/{flight.id_flight}", status_code=303)


@router.get("/delete/{flight_id}", response_class=HTMLResponse)
async def delete_flight(flight_id: int, request: Request, session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(Flight).where(Flight.id_flight == flight_id).options(selectinload(Flight.users))
    )
    return templates.TemplateResponse(
        "flight/flight_delete.html", {"request": request, "flight": result.scalars().first()}
    )


@router.post("/delete/{flight_id}", response_class=HTMLResponse)
async def delete_flight_submit(flight_id: int, request: Request, session: AsyncSession = Depends(get_session)):
    flight = await session.get(Flight, flight_id)
    if not flight:
        return RedirectResponse("/flights", status_code=303)

    try:
        await session.delete(flight)
        await session.commit()
    except Exception:
        await session.rollback()
        return RedirectResponse(f"/flights/delete/{flight_id}", status_code=303)

    return RedirectResponse("/flights/all", status_code=303)


@router.get("/add", response_class=HTMLResponse)
async def add_flight(request: Request, session: AsyncSession = Depends(get_session)):
    return templates.TemplateResponse("flight/flight_add.html", {"request": request, "flight": None})


@router.post("/add")
async def add_flight_submit(request: Request, session: AsyncSession = Depends(get_session)):
    form = await request.form()

    plate = (form.get("plate") or "").strip()  # type: ignore
    brand = (form.get("brand") or "").strip()  # type: ignore
    model = (form.get("model") or "").strip()  # type: ignore
    color = (form.get("color") or "").strip()  # type: ignore

    flight = Flight(plate=plate, brand=brand, model=model, color=color)
    session.add(flight)

    try:
        await session.commit()
    except Exception:
        await session.rollback()
        # при ошибке можно вернуть обратно на форму
        return RedirectResponse("/flights/add", status_code=303)

    return RedirectResponse(f"/flights/detail/{flight.id_flight}", status_code=303)
