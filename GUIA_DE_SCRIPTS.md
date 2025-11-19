# 📖 Guía Completa de Scripts de Inicio

## 🎯 Opciones Disponibles

Tienes **3 scripts diferentes** para iniciar el experimento. Elige según tus necesidades:

---

## 📁 Scripts Disponibles

### 1. `INSTALAR.bat` ⚙️
**Uso**: Solo la **primera vez**
**Qué hace**:
- Crea el entorno virtual
- Instala todas las dependencias (oTree, Django, etc.)
- Prepara todo para funcionar

**Cuándo usarlo**: Antes de usar cualquier otro script por primera vez

---

### 2. `INICIAR_CON_ENTORNO_VIRTUAL.bat` ✅ (RECOMENDADO)
**Uso**: Para correr el experimento con entorno virtual

**✅ Ventajas**:
- Aislado del sistema
- No interfiere con otras instalaciones de Python
- Versiones correctas de Django y oTree garantizadas
- **Profesional y seguro**

**📋 Características**:
- Activa automáticamente el entorno virtual
- Te pregunta: ¿localhost o red local?
- Opción 1: Solo en este computador (localhost)
- Opción 2: Red local (otros dispositivos pueden conectarse)
- Obtiene tu IP automáticamente
- Abre el navegador automáticamente

**Cuándo usarlo**:
- ✅ Uso normal del experimento
- ✅ Si ya corriste `INSTALAR.bat`
- ✅ Recomendado para uso profesional

---

### 3. `INICIAR_SIN_ENTORNO_VIRTUAL.bat` ⚠️
**Uso**: Para correr sin entorno virtual (Python global)

**⚠️ Advertencias**:
- Usa el Python instalado en el sistema
- **Requiere** que oTree esté instalado globalmente
- Puede tener conflictos de versiones
- No recomendado si no sabes qué versiones tienes instaladas

**📋 Características**:
- NO usa entorno virtual
- Te pregunta: ¿localhost o red local?
- Opción 1: Solo en este computador (localhost)
- Opción 2: Red local (otros dispositivos pueden conectarse)
- Obtiene tu IP automáticamente
- Abre el navegador automáticamente

**Cuándo usarlo**:
- ⚠️ Solo si el profesor YA tiene oTree instalado globalmente
- ⚠️ Si estás seguro de las versiones instaladas
- ⚠️ Si no quieres usar entorno virtual por alguna razón

---

### 4. `INICIAR_EXPERIMENTO.bat` 🚀 (Simple - Solo localhost)
**Uso**: Versión simple que solo abre en localhost

**📋 Características**:
- Usa entorno virtual
- Solo modo localhost (sin opciones)
- Más rápido (no pregunta nada)
- Ideal para pruebas rápidas

**Cuándo usarlo**:
- Si solo necesitas probar en tu computador
- No necesitas acceso desde otros dispositivos

---

## 🔄 Flujo de Trabajo Recomendado

### **Primera vez (Instalación)**:
```
1. Doble click en: INSTALAR.bat
   (Esperar 2-3 minutos mientras instala todo)

2. Doble click en: INICIAR_CON_ENTORNO_VIRTUAL.bat
   (Elegir opción 1 o 2 según necesites)
```

### **Usos posteriores**:
```
Doble click en: INICIAR_CON_ENTORNO_VIRTUAL.bat
(Elegir opción 1 o 2 según necesites)
```

---

## 🌐 ¿Localhost o Red Local?

### **Opción 1: LOCALHOST**
```
URL: http://localhost:8000
```
**Cuándo usar**:
- ✅ Solo tú vas a usar el experimento desde este computador
- ✅ Estás probando/desarrollando
- ✅ Modo demo con pestañas del navegador

**Ventajas**:
- Más rápido
- No necesitas configurar firewall
- Más seguro

---

### **Opción 2: RED LOCAL**
```
URL: http://192.168.X.X:8000 (tu IP local)
```
**Cuándo usar**:
- ✅ Varios estudiantes participarán desde sus celulares/tablets/computadores
- ✅ Experimento en laboratorio o aula
- ✅ Todos están en la misma red WiFi

**Requisitos**:
- ⚠️ Todos deben estar conectados a la **misma red WiFi**
- ⚠️ Puede que necesites desactivar el firewall de Windows
- ⚠️ Compartir la URL que aparece en pantalla con los participantes

**Pasos para participantes**:
1. Conectarse a la misma WiFi que el profesor
2. Abrir navegador en su dispositivo
3. Ingresar la URL que el profesor comparte (ej: http://192.168.1.100:8000)
4. Seguir los links de participante

---

## 🔥 Configuración de Firewall (Solo si usas Red Local)

Si eliges **Opción 2: Red Local** y otros no pueden conectarse:

### **Windows 10/11**:
1. Buscar "Firewall de Windows Defender"
2. Click en "Permitir una aplicación a través del firewall"
3. Click en "Cambiar configuración"
4. Click en "Permitir otra aplicación"
5. Buscar Python (ej: `C:\Python310\python.exe` o `venv\Scripts\python.exe`)
6. Marcar "Privada" y "Pública"
7. Click "Agregar"

### **Alternativa rápida** (temporal):
```
Desactivar temporalmente el firewall:
Panel de control → Firewall → Activar o desactivar
(¡No olvides reactivarlo después!)
```

---

## 📊 Comparación de Scripts

| Característica | INSTALAR.bat | INICIAR_CON_ENV.bat | INICIAR_SIN_ENV.bat | INICIAR_EXPERIMENTO.bat |
|---------------|--------------|---------------------|---------------------|------------------------|
| **Usa venv** | ✅ Crea | ✅ Sí | ❌ No | ✅ Sí |
| **Localhost** | N/A | ✅ Opción | ✅ Opción | ✅ Solo esto |
| **Red local** | N/A | ✅ Opción | ✅ Opción | ❌ No |
| **Auto IP** | N/A | ✅ Sí | ✅ Sí | ❌ No |
| **Instalación** | ✅ | ❌ | ❌ | ❌ |
| **Recomendado** | Primera vez | ✅ Siempre | ⚠️ Expertos | Pruebas |

---

## ❓ Preguntas Frecuentes

### **P: ¿Cuál script debo usar normalmente?**
R: `INICIAR_CON_ENTORNO_VIRTUAL.bat` (después de haber ejecutado `INSTALAR.bat` la primera vez)

### **P: ¿Qué es localhost?**
R: Es tu propio computador. Solo tú puedes acceder desde http://localhost:8000

### **P: ¿Cómo permito que otros accedan?**
R: Usa `INICIAR_CON_ENTORNO_VIRTUAL.bat`, elige opción 2 (Red Local), y comparte la IP que aparece

### **P: No puedo conectarme desde otro dispositivo**
R: Verifica:
1. Ambos están en la misma WiFi
2. Firewall de Windows permite Python
3. Estás usando la IP correcta que muestra el script

### **P: ¿Puedo borrar el entorno virtual?**
R: Sí, borra la carpeta `venv/` y vuelve a correr `INSTALAR.bat`

### **P: ¿Cuál es más rápido?**
R: `INICIAR_EXPERIMENTO.bat` (pero solo localhost, sin opciones)

---

## 🎯 Resumen Rápido

**Primer uso**:
```
INSTALAR.bat → INICIAR_CON_ENTORNO_VIRTUAL.bat
```

**Uso normal (solo tú)**:
```
INICIAR_CON_ENTORNO_VIRTUAL.bat → Opción 1
```

**Uso con estudiantes (red local)**:
```
INICIAR_CON_ENTORNO_VIRTUAL.bat → Opción 2
```

**Sin entorno virtual** (no recomendado):
```
INICIAR_SIN_ENTORNO_VIRTUAL.bat
```

---

¡Listo! Ahora puedes elegir el script que mejor se adapte a tus necesidades. 🚀
