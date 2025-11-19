# 📖 Guía Rápida para el Profesor

## 🚀 Instrucciones de Uso (3 Pasos)

### Primera vez (Solo una vez):

#### 1️⃣ **Instalar** (5 minutos)
- Haz doble click en: `INSTALAR.bat`
- Espera a que termine (se instala automáticamente)
- Cierra la ventana cuando diga "INSTALACIÓN COMPLETADA"

#### 2️⃣ **Iniciar Experimento**
- Haz doble click en: `INICIAR_CON_ENTORNO_VIRTUAL.bat`
- **Se te preguntará**: ¿Localhost o Red Local?
  - **Opción 1**: Solo en tu computador (para pruebas)
  - **Opción 2**: Red local (para que estudiantes se conecten desde sus dispositivos)

#### 3️⃣ **Crear Sesión**
- **Usuario**: `admin`
- **Contraseña**: `admin123`
- Click en "Sessions" → "Create new session"
- Seleccionar "plott_sunder"
- Número de participantes: **múltiplo de 3** (ej: 3, 6, 9, 12, 15, etc.)
- Click "Create"
- Compartir los links con los estudiantes

---

## 🔄 Usos Posteriores

Simplemente haz doble click en: `INICIAR_CON_ENTORNO_VIRTUAL.bat`

**No necesitas volver a instalar.**

---

## 🌐 ¿Qué opción elegir?

### **Opción 1: LOCALHOST** (Solo tu computador)
✅ Úsala para:
- Probar el experimento
- Modo demo
- Hacer pruebas antes de la clase

### **Opción 2: RED LOCAL** (Estudiantes con sus dispositivos)
✅ Úsala para:
- Experimento real en clase
- Estudiantes usan sus celulares/tablets/laptops
- Todos deben estar en la **misma red WiFi**

**Importante**: Cuando elijas opción 2, el script mostrará una URL como:
```
http://192.168.1.100:8000
```
**Comparte esta URL con tus estudiantes** para que se conecten.

---

## 📝 Scripts Disponibles

### Scripts Principales:

1. **`INSTALAR.bat`** - Primera vez (instala todo)
2. **`INICIAR_CON_ENTORNO_VIRTUAL.bat`** - ✅ **RECOMENDADO** (con opciones localhost/red)
3. **`INICIAR_SIN_ENTORNO_VIRTUAL.bat`** - ⚠️ Solo si ya tienes oTree instalado
4. **`INICIAR_EXPERIMENTO.bat`** - Versión simple (solo localhost)

**Ver detalles**: Lee `GUIA_DE_SCRIPTS.md` para comparación completa

---

## ⚙️ Características del Experimento

- **5 rondas** en total
- **3 jugadores por grupo**
- **Rondas 1-3**: Predicciones sin información adicional
- **Rondas 4-5**: Los jugadores ven estadísticas agregadas del grupo (promedio, mínimo, máximo de rondas 1-3)
- **1000 puntos** por ronda al mejor predictor
- **Máximo**: 5000 puntos totales

---

## 🛑 Detener el Servidor

En la ventana negra que se abre, presiona: `Ctrl + C`

---

## ❓ Problemas Comunes

### "Python no está instalado"
→ Instalar Python 3.8+ desde [python.org](https://www.python.org/downloads/)
→ Durante la instalación, marcar "Add Python to PATH"

### "No abre el navegador"
→ Ir manualmente a: `http://localhost:8000`

### "Puerto en uso"
→ Cerrar otras ventanas de servidor que estén corriendo
→ O reiniciar el computador

---

## 📂 Archivos Importantes

- `INSTALAR.bat` → Instala todo automáticamente (solo 1 vez)
- `INICIAR_EXPERIMENTO.bat` → Inicia el experimento (cada vez que lo uses)
- `requirements.txt` → Dependencias del proyecto
- `plott_sunder/` → Código del experimento

---

## 🔒 Seguridad

**Importante**: Este experimento usa un entorno virtual que:
- ✅ **No afecta** otras instalaciones de Python en tu computador
- ✅ **Aísla** las dependencias del proyecto
- ✅ Es la **mejor práctica** profesional
- ✅ Se puede borrar completamente sin afectar nada más (carpeta `venv/`)

---

## 📧 Soporte

Si hay problemas técnicos, contactar al desarrollador del proyecto.

---

## 🎓 Uso Pedagógico

Este experimento enseña:
- Información asimétrica
- Agregación de información en mercados
- Inferencia bayesiana
- Efecto de información pública en decisiones

**Concepto clave de rondas 4-5**: Al ver las estadísticas agregadas del grupo, los estudiantes pueden observar cómo la información pública afecta sus decisiones, ilustrando el concepto de agregación de información de Plott & Sunder (1988).
