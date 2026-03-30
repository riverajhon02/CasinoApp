#  Guía de Contribución

Gracias por contribuir a este proyecto  
A continuación encontrarás la estructura de ramas, convención de commits y flujo de trabajo oficial.

---

#  Estrategia de Ramas (Git Flow Simplificado)

## Ramas Principales

- `main` → Rama estable en producción.

## Ramas de Trabajo

Se crean a partir de `main`

| Tipo      | Prefijo     | Ejemplo |
|-----------|------------|----------|
| Feature   | `feature/` | `feature/123-login-validation` |
| Fix       | `fix/`     | `fix/145-login-error` |
| Refactor  | `refactor/`| `refactor/210-user-service` |
| Docs      | `docs/`    | `docs/300-update-readme` |
| Test      | `test/`    | `test/410-auth-tests` |

 **Estructura obligatoria:**
```
tipo/numero_issue-descripcion-corta
```

Ejemplo:
```
feature/123-login-validation
```

---

#  Convención de Commits

Usamos una convención estándar para mantener el historial limpio y profesional.

## Tipos Permitidos

- `feat:` Nueva funcionalidad
- `fix:` Corrección de errores
- `refactor:` Mejora interna sin cambiar funcionalidad
- `docs:` Cambios en documentación
- `test:` Agregar o modificar pruebas

## Ejemplo de Commit

```bash
git commit -m "feat: agrega validación de login (#123)"
```

 Siempre incluir el número del issue entre paréntesis.

---

#  Flujo de Trabajo Paso a Paso

## 1 Actualizar tu rama local

```bash
git checkout main
git pull origin main
```

---

## 2️ Crear rama del issue asignado

```bash
git checkout -b feature/123-login-validation
```

---

## 3️ Desarrollar la funcionalidad

Realiza los cambios necesarios siguiendo las buenas prácticas del proyecto.

---

## 4️ Agregar cambios y hacer commit

```bash
git add .
git commit -m "feat: agrega validación de login (#123)"
```

---

## 5️ Subir la rama al repositorio remoto

```bash
git push origin feature/123-login-validation
```

---

## 6️ Crear Pull Request

- Ir al repositorio en GitHub.
- Crear Pull Request hacia `main`.
- Asignar revisores.
- Vincular el issue correspondiente.

---

## 7️ Revisión de Código

- Esperar comentarios.
- Realizar ajustes si son solicitados.
- Subir nuevos commits si es necesario.

---

## 8️ Merge

Una vez aprobado el Pull Request:
- Se realiza el merge a `main`.
- El issue se cierra.

---

## 9️ Actualizar tu rama local después del merge

```bash
git checkout main
git pull origin main
```

---

##  Eliminar rama de trabajo

### Eliminar rama remota

```bash
git push origin --delete feature/123-login-validation
```

### Eliminar rama local

```bash
git branch -d feature/123-login-validation
```

---

#  Buenas Prácticas

✔ No trabajar directamente sobre `main`  
✔ Hacer commits pequeños y descriptivos  
✔ Probar antes de subir cambios  
✔ Mantener código limpio y formateado  
✔ Seguir la convención de nombres  
✔ Referenciar siempre el número del issue  

---

#  Reglas Importantes

- Todo cambio debe pasar por Pull Request.
- No se permite hacer push directo a `main`.
- El código debe estar probado antes de solicitar revisión.
- Mantener coherencia en nombres y estructura.

---

#  Objetivo

Mantener un flujo de trabajo ordenado, profesional y escalable para facilitar la colaboración en equipo.
