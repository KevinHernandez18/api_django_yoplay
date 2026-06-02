# api_django_yoplay

Repositorio con APIs REST de tipo CRUD para los diferentes esquemas del proyecto YoPLAY.

Cada carpeta contiene un proyecto Django independiente con Django REST Framework. Los endpoints estan construidos con `ModelViewSet`, por lo que cada recurso soporta las operaciones CRUD habituales.

Ejemplos reales de rutas CRUD:

- `GET /api/torneos/`: listar torneos.
- `POST /api/torneos/`: crear un torneo.
- `GET /api/torneos/1/`: consultar el torneo con ID `1`.
- `PUT /api/torneos/1/`: actualizar completo el torneo con ID `1`.
- `PATCH /api/torneos/1/`: actualizar parcialmente el torneo con ID `1`.
- `DELETE /api/torneos/1/`: eliminar el torneo con ID `1`.
- `GET /gestion_encuentro/encuentros/`: listar encuentros.
- `GET /api/usuario/`: listar usuarios.
- `GET /api/tutoriales/`: listar tutoriales.

## Paginacion

Los esquemas tienen paginacion por numero de pagina. Cuando se usa la clase `DefaultPageNumberPagination`, el comportamiento es:

- Tamano por defecto: `10` registros.
- Parametro para cambiar tamano: `page_size`.
- Tamano maximo: `100` registros.
- Para traer todos los registros sin paginar, usa `?page_size=-1` en el endpoint de lista.

Ejemplos:

```text
GET /gestion_encuentro/encuentros/?page_size=3
GET /gestion_encuentro/encuentros/?page=2&page_size=3
GET /gestion_encuentro/encuentros/?page_size=-1
GET /api/torneos/?page_size=-1
GET /api/usuario/?page_size=-1
```

## api_crud_djnago_clase

Proyecto para catalogos base de reglas, deportes, distribuciones y reglamentos.

Ruta base de la API:

```text
/api/
```

Swagger:

```text
/swagger/
```

### Modelos y funcionalidades

#### Reglas

Tabla: `reglas`

Permite administrar reglas generales.

Campos principales:

- `id_reglas`
- `cantidad_reglas`
- `descripcion`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Endpoint:

```text
/api/Reglas/
```

Para traer todos los registros:

```text
/api/Reglas/?page_size=-1
```

#### Tipo_deporte

Tabla: `tipo_deporte`

Permite administrar tipos de deporte.

Campos principales:

- `id_tipo_deporte`
- `nombre_deporte`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Endpoint:

```text
/api/Tipo_deporte/
```

Para traer todos los registros:

```text
/api/Tipo_deporte/?page_size=-1
```

#### Tipo_distribucion

Tabla: `tipo_distribucion`

Permite administrar tipos de distribucion o forma de organizacion de equipos.

Campos principales:

- `id_tipo_distribucion`
- `equipo`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Endpoint:

```text
/api/Tipo_distribucion/
```

Para traer todos los registros:

```text
/api/Tipo_distribucion/?page_size=-1
```

#### Tipo_reglamento

Tabla: `tipo_reglamento`

Permite administrar categorias o tipos de reglamento asociados a un deporte.

Campos principales:

- `id_tipo_reglamento`
- `id_tipo_deporte`
- `nombre_tipo`
- `descripcion`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Relacion:

- `id_tipo_deporte` referencia a `Tipo_deporte`.

Endpoint:

```text
/api/Tipo_reglamento/
```

Para traer todos los registros:

```text
/api/Tipo_reglamento/?page_size=-1
```

## api_crud_djnago_gestion_deportiva

Proyecto para la gestion deportiva principal: equipos, torneos, premiaciones, reglamentos, integrantes, clasificacion e historial.

Ruta base de la API:

```text
/api/
```

Swagger:

```text
/swagger/
```

### Modelos y funcionalidades

#### Equipo

Tabla: `equipo`

Permite administrar equipos deportivos.

Campos principales:

- `id_equipo`
- `nombre_equipo`
- `categoria`
- `cantidad_jugadores`
- `region`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Endpoint:

```text
/api/equipos/
```

Para traer todos los registros:

```text
/api/equipos/?page_size=-1
```

#### Premiacion

Tabla: `premiacion`

Permite administrar premios o premiaciones de torneos.

Campos principales:

- `id_premiacion`
- `cantidad_premiacion`
- `descripcion`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Endpoint:

```text
/api/premiaciones/
```

Para traer todos los registros:

```text
/api/premiaciones/?page_size=-1
```

#### Torneo

Tabla: `torneo`

Permite administrar torneos deportivos.

Campos principales:

- `id_torneo`
- `id_tipo_deporte`
- `nombre_torneo`
- `fecha_inicio`
- `fecha_fin`
- `ubicacion`
- `objetivo`
- `fecha_fase`
- `cantidad_equipo`
- `id_tipo_distribucion`
- `id_premiacion`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Relacion:

- `id_premiacion` referencia a `Premiacion`.

Endpoint:

```text
/api/torneos/
```

Para traer todos los registros:

```text
/api/torneos/?page_size=-1
```

#### Imagen

Tabla: `imagen`

Permite administrar imagenes asociadas a torneos.

Campos principales:

- `id_imagen`
- `id_torneo`
- `url_imagen`
- `tipo_imagen`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Relacion:

- `id_torneo` referencia a `Torneo`.

Endpoint:

```text
/api/imagenes/
```

Para traer todos los registros:

```text
/api/imagenes/?page_size=-1
```

#### Distribucion

Tabla: `distribucion`

Permite administrar la distribucion de un torneo.

Campos principales:

- `id_distribucion`
- `id_torneo`
- `id_tipo_distribucion`
- `confirmacion`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Relacion:

- `id_torneo` referencia a `Torneo`.

Endpoint:

```text
/api/distribuciones/
```

Para traer todos los registros:

```text
/api/distribuciones/?page_size=-1
```

#### Reglamento

Tabla: `reglamento`

Permite administrar reglamentos asociados a torneos.

Campos principales:

- `id_reglamento`
- `id_torneo`
- `id_tipo_reglamento`
- `id_reglas`
- `id_tipo_deporte`
- `idioma`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Relacion:

- `id_torneo` referencia a `Torneo`.

Endpoint:

```text
/api/reglamentos/
```

Para traer todos los registros:

```text
/api/reglamentos/?page_size=-1
```

#### Integrante

Tabla: `integrantes`

Permite administrar integrantes de equipos.

Campos principales:

- `id_integrante`
- `id_equipo`
- `nombre`
- `posicion`
- `correo`
- `telefono`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Relacion:

- `id_equipo` referencia a `Equipo`.

Endpoint:

```text
/api/integrantes/
```

Para traer todos los registros:

```text
/api/integrantes/?page_size=-1
```

#### Clasificacion

Tabla: `clasificacion`

Permite administrar estadisticas y puntos por equipo dentro de torneos.

Campos principales:

- `id_clasificacion`
- `id_encuentro`
- `partido_jugado`
- `partido_ganado`
- `partido_empatado`
- `partido_derrota`
- `puntos_partidos`
- `id_torneo`
- `id_equipo`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Relaciones:

- `id_torneo` referencia a `Torneo`.
- `id_equipo` referencia a `Equipo`.

Endpoint:

```text
/api/clasificaciones/
```

Para traer todos los registros:

```text
/api/clasificaciones/?page_size=-1
```

#### HistorialTorneos

Tabla: `historialtorneos`

Permite guardar informacion historica de torneos y su estado.

Campos principales:

- `id_historial`
- `nombre_torneo`
- `id_torneo`
- `id_usuario`
- `deporte`
- `reglamento`
- `equipos`
- `id_tipo_distribucion`
- `distribucion`
- `estado`
- `finalizacion`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Relacion:

- `id_torneo` referencia a `Torneo`.

Endpoint:

```text
/api/historialtorneos/
```

Para traer todos los registros:

```text
/api/historialtorneos/?page_size=-1
```

## gestion_encuentro

Proyecto para gestionar encuentros, grupos y resultados por equipo.

Ruta base de la API:

```text
/gestion_encuentro/
```

Swagger:

```text
/gestion_encuentro/swagger/
```

### Modelos y funcionalidades

#### encuentro

Tabla: `encuentro`

Permite administrar encuentros entre dos equipos dentro de un torneo.

Campos principales:

- `id_encuentro`
- `fecha`
- `id_torneo`
- `id_tipo_distribucion`
- `fase_torneo`
- `id_equipo_1`
- `resultado_equipo_1`
- `id_equipo_2`
- `resultado_equipo_2`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Valores permitidos para `fase_torneo`:

- `Grupos`
- `Octavos`
- `Cuartos`
- `Semifinal`
- `Final`

Valores permitidos para resultados:

- `Ganador`
- `Perdedor`
- `Empate`

Endpoint:

```text
/gestion_encuentro/encuentros/
```

Para traer todos los encuentros sin paginacion:

```text
/gestion_encuentro/encuentros/?page_size=-1
```

#### grupo

Tabla: `grupo`

Permite administrar grupos de competencia.

Campos principales:

- `id_grupo`
- `grupo`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Endpoint:

```text
/gestion_encuentro/grupos/
```

Para traer todos los grupos sin paginacion:

```text
/gestion_encuentro/grupos/?page_size=-1
```

#### grupo_encuentro

Tabla: `grupo_encuentro`

Permite asociar encuentros a grupos.

Campos principales:

- `id_grupo_encuentro`
- `id_grupo`
- `id_encuentro`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Relaciones:

- `id_grupo` referencia a `grupo`.
- `id_encuentro` referencia a `encuentro`.

Endpoint:

```text
/gestion_encuentro/grupo_encuentros/
```

Para traer todos los registros de grupo-encuentro sin paginacion:

```text
/gestion_encuentro/grupo_encuentros/?page_size=-1
```

#### grupo_equipo

Tabla: `grupo_equipo`

Permite asociar equipos a grupos y registrar estadisticas basicas.

Campos principales:

- `id_grupo_equipo`
- `id_grupo`
- `id_equipo`
- `partidos_jugados`
- `empates`
- `victorias`
- `derrotas`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Relacion:

- `id_grupo` referencia a `grupo`.

Endpoint:

```text
/gestion_encuentro/grupo_equipos/
```

Para traer todos los registros de grupo-equipo sin paginacion:

```text
/gestion_encuentro/grupo_equipos/?page_size=-1
```

## schema_tutoriales

Proyecto para administrar tutoriales y autenticacion JWT.

Ruta base de la API:

```text
/api/
```

Swagger:

```text
/swagger/
```

### Modelos y funcionalidades

#### Tutoriales

Tabla: `tutoriales`

Permite administrar tutoriales publicados.

Campos principales:

- `id_tutoriales`
- `titulo`
- `descripcion`
- `link_tuturial`
- `fecha_publication`
- `fecha_creacion`
- `fecha_modificacion`
- `activo`

Endpoint:

```text
/api/tutoriales/
```

Para traer todos los registros:

```text
/api/tutoriales/?page_size=-1
```

### Autenticacion

Endpoints JWT configurados:

```text
/api/auth/login/
/api/auth/token/
```

Ambos usan `TokenObtainPairView`.

## schema_usuario

Proyecto para administrar documentos, usuarios, contrasenas e historial de acceso.

Ruta base de la API:

```text
/api/
```

Swagger:

```text
/swagger/
```

### Modelos y funcionalidades

#### Documento

Tabla: `documento`

Permite administrar tipos de documento.

Campos principales:

- `id_Documento`
- `tipo_documento`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Endpoint:

```text
/api/documento/
```

Para traer todos los registros:

```text
/api/documento/?page_size=-1
```

#### Usuario

Tabla: `usuario`

Permite administrar usuarios.

Campos principales:

- `id_usuario`
- `documento`
- `nombre`
- `apellido`
- `numero_documento`
- `email`
- `telefono`
- `fecha_nacimiento`
- `fecha_registro`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Relacion:

- `documento` referencia a `Documento`.

Endpoint:

```text
/api/usuario/
```

Para traer todos los registros:

```text
/api/usuario/?page_size=-1
```

#### Contrasena

Tabla: `contrasena`

Permite administrar contrasenas asociadas a usuarios.

Campos principales:

- `id_contrasena`
- `usuario`
- `contrasena`
- `hash_contrasena`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Relacion:

- `usuario` referencia a `Usuario`.

Endpoint:

```text
/api/contrasena/
```

Para traer todos los registros:

```text
/api/contrasena/?page_size=-1
```

#### HistorialAcceso

Tabla: `historial_acceso`

Permite registrar intentos de acceso de usuarios.

Campos principales:

- `id_historial_acceso`
- `usuario`
- `contrasena`
- `fecha_intento`
- `exitoso`
- `ip_origen`
- `fallo_motivo`
- `activo`
- `fecha_creacion`
- `fecha_modificacion`

Relaciones:

- `usuario` referencia a `Usuario`.
- `contrasena` referencia a `Contrasena`.

Endpoint:

```text
/api/historial_acceso/
```

Para traer todos los registros:

```text
/api/historial_acceso/?page_size=-1
```

## Notas tecnicas

- Los serializers usan `fields = '__all__'`, por lo que exponen todos los campos definidos en cada modelo.
- Los endpoints registrados con `DefaultRouter` generan automaticamente rutas de lista y detalle.
- Varios modelos usan campos enteros para IDs de tablas externas a su esquema, por ejemplo `id_torneo`, `id_equipo`, `id_tipo_deporte`, `id_tipo_distribucion`, `id_reglas` o `id_usuario`.
- Algunos proyectos tienen configuracion de paginacion personalizada en archivos `pagination.py`.
