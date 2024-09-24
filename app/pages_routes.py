from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse




page_router = APIRouter()

# Jinja2 templates
templates = Jinja2Templates(directory="app/templates")


@page_router.get("/", response_class=HTMLResponse, name="home")
async def home_page(request:Request):
   
    return templates.TemplateResponse(name ="home.html", request = request)


@page_router.get("/about", response_class=HTMLResponse, name="about")
async def about_page(request:Request):
    return templates.TemplateResponse(name = "aboutus.html", request = request)


@page_router.get("/rates", response_class=HTMLResponse, name="rate")
async def roomsandrates_page(request:Request):
    return templates.TemplateResponse(name = "roomsandrates.html", request = request)



@page_router.get("/offers", response_class=HTMLResponse, name="offers")
async def vipoffers_page(request:Request):
    return templates.TemplateResponse(name = "vipoffers.html", request = request)


@page_router.get("/location", response_class=HTMLResponse, name="location")
async def location_page(request:Request):
    return templates.TemplateResponse(name = "location.html", request = request)
