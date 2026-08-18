# 01-project — guía para Claude Code

Aplicación Angular + TypeScript con base de datos MySQL (ver carpeta DB/).

## Protocolo de trabajo (handoff + Git)

Aplica a todo el que trabaje en este repositorio, use Claude Code o no. El trabajo se
reparte entre varias máquinas y varios desarrolladores, así que la continuidad y la
coordinación son parte del trabajo, no un extra.

### Handoff

1. **Al iniciar cualquier sesión**: leer `handoff.md` COMPLETO antes de tocar código.
   Contiene el objetivo, el estado real y el punto exacto donde quedó la sesión
   anterior. Continuar desde ahí; no re-descubrir el proyecto desde cero.
2. **Si `handoff.md` todavía no existe**, crearlo en cuanto empiece trabajo real, con
   las 8 secciones de abajo, y hacerle commit + push.
3. **Antes de cerrar la sesión** (cuando el usuario se despida, diga que va a cerrar, o
   pida «actualiza el handoff»): actualizarlo con lo ocurrido manteniendo sus 8
   secciones, actualizar la fecha de «Última actualización», y hacer commit + push para
   que el otro equipo siempre lo reciba.
4. Si se termina un bloque de trabajo significativo a mitad de sesión, actualizar el
   handoff también — no esperar al cierre.

Las 8 secciones fijas de `handoff.md`:

1. El objetivo
2. El estado actual del proyecto
3. Los archivos en los que trabajas
4. Qué has cambiado
5. Qué has intentado
6. Qué ha fallado
7. Qué planeas hacer después
8. Cualquier cosa relevante

### Git y GitHub

- **Commit + push de todo cambio**, sin esperar a que el usuario lo pida cada vez.
- En **lotes grandes**: presentar primero un resumen y esperar el visto bueno del
  usuario antes del push.
- Trabajar sobre la rama que ya use el repo. No crear ramas nuevas salvo que se pida.
- **Cambios remotos: avisar y PREGUNTAR antes de hacer `pull`.** Nunca traer cambios de
  otros desarrolladores sin confirmación, porque puede pisar trabajo local en curso.
  Conviene un `git fetch` al empezar para saber si hay novedades.
- Mensajes de commit en español, explicando el porqué del cambio.
- **Nunca versionar `.env` ni credenciales**, ni ponerlas en archivos de ejemplo,
  instaladores o scripts. Revisar `.gitignore` antes del primer push.
- No reescribir historia ya publicada (`push --force`, `reset --hard` sobre lo subido)
  sin pedirlo explícitamente: hay otras personas trabajando sobre el mismo remoto.
