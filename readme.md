## API FOMO
------------------------------------------------------------------------------------------

#### Consultar Eventos


<details>
 <summary><code>GET</code> <code><b>/event</b></code> <code>Eventos</code></summary>

##### Parameters

> | name         | type                   | data type           | description                  |
> |--------------|------------------------|---------------------|------------------------------|
> | `start_date` | optional               | date (DD-MM-YYYY)   | start_date                   |
> | `end_date`   | optional               | date (DD-MM-YYYY)   | end_date                     |
> | `free`       | optional               | str                 | si es grati                  |
> | `category`   | optional x N categorys | list                | The specific stub numeric id |
> | `event_name` | optional               | str                 | The specific stub numeric id |
> 
> 
> 
> 

##### Responses

> | http code     | content-type                      | response |
> |---------------|-----------------------------------|----------|
> | `200`         | `application/json`        | Json     |

##### Example Response
```json
[
    {
        "id": 1,
        "end_date": "2024-07-31 17:09:38",
        "start_date": "2023-08-31 17:09:35",
        "day_name_start": "Jueves",
        "day_name_end": "Miércoles",
        "event_name": "Prueba después de migrate",
        "event_img": "http://127.0.0.1:8000/media/images/Screenshot_from_2023-07-30_17-24-56.png",
        "image_url": "/media/images/Screenshot_from_2023-07-30_17-24-56.png",
        "event_location": "En lo de tu señora",
        "ticket_price": null,
        "highlighted": false,
        "category": "teatro"
    },
    {
        "id": 2,
        "start_date": "2024-08-02 23:05:24",
        "end_date": "2025-08-02 23:05:29",
        "day_name_start": "Viernes",
        "day_name_end": "Sábado",
        "event_name": "Prueba 2-8-23",
        "event_img": "http://127.0.0.1:8000/media/images/Screenshot_from_2023-07-30_17-24-56_3R4AIZD.png",
        "image_url": "/media/images/Screenshot_from_2023-07-30_17-24-56_3R4AIZD.png",
        "event_location": "En lo de tu señora 2",
        "ticket_price": null,
        "highlighted": false,
        "category": "musica"
    }
]
```



</details>

<details>
 <summary><code>GET</code> <code><b>/event/ID</b></code> <code>Eventos</code></summary>

##### Parameters

> | name |  type     | data type      | description                         |
> |------|-----------|----------------|-------------------------------------|
> | `id`  |  required | int ($int64)   | The specific stub numeric id        |

##### Responses

> | http code | content-type                      | response                                    |
> |-----------|-----------------------------------|---------------------------------------------|
> | `200`     | `application/json`        | Json                                        |
> | `404`     | `application/json`                | `{"code":"404","detail": "No encontrado."}` |


##### Example Response
```json
{
    "id": 7,
    "day_name_start": "Viernes",
    "day_name_end": "Lunes",
    "start_date": "2029-08-03T14:45:07Z",
    "end_date": "2043-08-03T14:45:09Z",
    "event_name": "free y category",
    "has_ticket": true,
    "ticket_price": 0,
    "tickets_left": true,
    "tickets_available": 1000,
    "buy_tickets": "asdsad",
    "event_link": "asdasd",
    "event_img": "http://127.0.0.1:8000/media/images/Screenshot_from_2023-07-31_14-46-30_Qc4V83u.png",
    "organization_page": "asdasdsad",
    "event_location": "En lo de tu señora 8",
    "highlighted": false,
    "user_creator": 1,
    "category": "Obra de teatro"
}
```

</details>


------------------------------------------------------------------------------------------

#### Consultar Categorias


<details>
 <summary><code>GET</code> <code><b>/category</b></code> <code>Categorias</code></summary>

##### Parameters

> | name |  type     | data type      | description                         |
> |------|-----------|----------------|-------------------------------------|

##### Responses

> | http code | content-type                      | response                                    |
> |-----------|-----------------------------------|---------------------------------------------|
> | `200`     | `application/json`        | Json                                        |

##### Example Response
```json
[
    {
        "id": 1,
        "name": "teatro"
    },
    {
        "id": 2,
        "name": "musica"
    },
    {
        "id": 3,
        "name": "perreo"
    }
]
```

</details>


<details>
 <summary><code>GET</code> <code><b>/category/id</b></code> <code>Categorias</code></summary>

##### Parameters

> | name |  type     | data type      | description                         |
> |------|-----------|----------------|-------------------------------------|
> | `id`  |  required | int ($int64)   | The specific stub numeric id        |

##### Responses

> | http code | content-type                      | response                                    |
> |-----------|-----------------------------------|---------------------------------------------|
> | `200`     | `application/json`        | Json                                        |
> | `404`     | `application/json`                | `{"code":"404","detail": "No encontrado."}` |

##### Example Response
```json
[
    {
        "id": 1,
        "name": "teatro"
    }
]
```

</details>

------------------------------------------------------------------------------------------

#### Consultar Carruseles

<details>
 <summary><code>GET</code> <code><b>/carousel</b></code> <code>Carruseles</code></summary>

##### Parameters

> | name |  type     | data type      | description                         |
> |------|-----------|----------------|-------------------------------------|

##### Responses

> | http code | content-type                      | response                                    |
> |-----------|-----------------------------------|---------------------------------------------|
> | `200`     | `application/json`        | Json                                        |

##### Example Response
```json
[
    {
        "order": 2,
        "name": "asdasdsa",
        "description": "dasdasdsad",
        "image_short": "/media/images/Screenshot_from_2023-08-04_09-08-49.png",
        "description_button": "dasfdsfdsaf",
        "link_button": "asdfsadfsdafdsaf"
    },
    {
        "order": 5,
        "name": "josé el carrusel",
        "description": "carruseliente",
        "image_short": "/media/images/Screenshot_from_2023-08-03_13-51-05.png",
        "description_button": "clickee aquí buen jombre",
        "link_button": "www.hola.com"
    },
    {
        "order": 6,
        "name": "pepe",
        "description": "popo",
        "image_short": "/media/images/Screenshot_from_2023-08-03_11-56-57.png",
        "description_button": "pupu",
        "link_button": "prrrr"
    }
]
```

</details>