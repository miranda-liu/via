import mapboxgl from 'mapbox-gl';

mapboxgl.accessToken = '<pk.eyJ1Ijoicmt1YmEiLCJhIjoiY2xtbDZtbnBtMDg3MzJrbW9jNTJqMzVibiJ9.1G7FCXA5MdikERXLIAuJLQ>';
const map = new mapboxgl.Map({
    container: 'map', // container ID
    style: 'mapbox://styles/mapbox/streets-v12', // style URL
    center: [-74.5, 40], // starting position [lng, lat]
    zoom: 9 // starting zoom
});