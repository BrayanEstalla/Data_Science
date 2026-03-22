# Gestor de Paquetes de Python: PyPI y pip

## ¿Qué es PyPI?

**PyPI (Python Package Index)** es el repositorio oficial de paquetes de Python.  
Funciona como una gran biblioteca en línea donde desarrolladores de todo el mundo publican librerías y herramientas que otros programadores pueden reutilizar en sus proyectos.

Sitio oficial: https://pypi.org

En PyPI se encuentran miles de paquetes para diferentes propósitos, por ejemplo:

- **Data Science:** `numpy`, `pandas`, `scikit-learn`
- **Machine Learning / Deep Learning:** `tensorflow`, `torch`
- **Desarrollo Web:** `django`, `flask`, `fastapi`
- **Visualización:** `matplotlib`, `seaborn`, `plotly`

Gracias a PyPI, los desarrolladores no necesitan escribir todo desde cero; pueden instalar paquetes ya creados y utilizarlos fácilmente.

---

# ¿Qué es pip?

**pip** es el gestor de paquetes de Python que permite **instalar, actualizar y eliminar paquetes desde PyPI**.

Generalmente viene instalado automáticamente con Python.

Para verificar si `pip` está instalado:

```
pip --version
```

para trabajar con pip se recomienda crear primero un entorno virtual

## como crear un entorno virtual

### paso 1 - creamos el entorno virtual
```
python -m venv venv
```

### paso 2 - activamos el entorno virtual
```
En linux o Machine
source venv/Scripts/activate 

En Windows
No se puede cargar el archivo C:\Users\abc\venv\Scripts\Activate.ps1 porque
la ejecución de scripts está deshabilitada en este sistema.
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process (Solo esa sesión)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine (permanente - PowerShell - administrador)
venv\Scripts\activate
```