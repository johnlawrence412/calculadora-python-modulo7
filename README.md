# Calculadora en Python – Módulo 7

- `Operaciones.py`: módulo con las funciones matemáticas.
- `main.py`: programa principal que interactúa con el usuario.

---

## Funcionalidad

La calculadora permite trabajar con dos números reales y realizar:

- **Suma(1)**
- **Resta(2)**
- **Multiplicación(3)**
- **División(4)**

En el menú, la operación se muestra con el formato:

```text
Suma(1)
Resta(2)
Multiplicación(3)
División(4)
````

El usuario puede escribir **el número o el nombre** de la operación
(por ejemplo: `1` o `suma`, `2` o `resta`, etc.).

---

## Estructura del código

### `Operaciones.py`

Contiene las funciones:

* `sumar(a, b)`
* `restar(a, b)`
* `multiplicar(a, b)`
* `dividir(a, b)` → valida que el divisor no sea cero y lanza `ValueError` si `b == 0`.

### `main.py`

* Pide al usuario los dos números.
* Muestra el menú de operaciones con el formato `Suma(1)`, `Resta(2)`, etc.
* Permite ingresar la operación por número o por nombre.
* Llama a la función correspondiente del módulo `Operaciones`.
* Muestra el resultado en pantalla.
* Incluye validaciones:

  * Manejo de entradas no numéricas usando `try/except`.
  * Verificación de que la operación exista.
  * Manejo de división entre cero capturando la excepción de `Operaciones.dividir`.
* Utiliza un bucle para que el usuario pueda realizar varias operaciones hasta que decida salir.

---

## Requisitos

* Python 3.x instalado en el sistema.

---

## Cómo ejecutar el programa

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/johnlawrence412/calculadora-python-modulo7.git
   cd calculadora-python-modulo7
   ```

2. Ejecutar el archivo principal:

   ```bash
   python main.py
   ```

3. Seguir las instrucciones en pantalla:

   * Ingresar los dos números.
   * Elegir la operación (por número o por nombre).
   * Decidir si desea realizar otra operación o salir.
