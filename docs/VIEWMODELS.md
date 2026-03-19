# ViewModels
Es el puente entre los Modelos o Servicios y las Vistas.

## AccountHubViewModel

* **`list[Account] accounts`**: Lista de cuentas disponibles en la base de datos.
* **`load_accounts()`**: Carga las cuentas desde la base de datos y las guarda en `accounts`.

---

## AccountEditorViewModel(`Account? account`)

> **Inicialización:** Si `account` tiene un valor, se asigna a `self.account` para su edición; de lo contrario, se inicializa con un valor por defecto para la creación de una nueva cuenta.
* **`Account account`**: Cuenta que está siendo manipulada.
* **`change_account_name(string value)`**: Cambia el atributo `name` de la cuenta.
* **`change_account_currency(string value)`**: Cambia el atributo `currency` de la cuenta.
* **`save_account()`**: Guarda la cuenta en la base de datos.

---

## SettingsViewModel

* **`list[ThemeMode] theme_modes`**: Lista de los modos de tema disponibles.
* **`change_theme_mode(ThemeMode value)`**: Actualiza el modo de tema de la aplicación.

---

## CategoryHubViewModel

* **`list[Category] categories`**: Lista de categorías disponibles en la base de datos.
* **`load_categories()`**: Carga las categorías desde la base de datos y las guarda en `categories`.
* **`delete_category(int index)`**: Elimina la categoría tanto de la lista en memoria como de la base de datos, basándose en su posición en la colección actual.

---

## CategoryEditorViewModel(`Category? category`)

> **Inicialización:** Si `category` tiene un valor, se asigna a `self.category` para su edición; de lo contrario, se inicializa con un valor por defecto para la creación de una nueva categoría.

* **`Category category`**: Instancia de la categoría que está siendo manipulada.
* **`change_category_name(string value)`**: Actualiza de forma reactiva el atributo `name` de la categoría.
* **`change_category_type(string value)`**: Actualiza de forma reactiva el atributo `type` de la categoría.
* **`save_category()`**: Guarda la categoría en la base de datos.

---

## AccountDashboardViewModel(`Account account`)
> **Inicialización:** Se asigna `account` a `self.account`.
`Account account`: Cuenta seleccionada.

---

## AccountHomeVieModel(`Account account`)
> **Inicialización:** Se asigna `account` a `self.account`.

* **`Account account`**: Cuenta a tratar.
* **`int year`**: Representación del año que se inicializa con el año actual.
* **`int month`**: Representación del mes que se inicializa con el mes actual
* **`Decimal income`**: Ingreso total de la cuenta del mes y año actual
* **`Decimal expenses`**: Gasto total de la cuenta del mes y año actual
* **`Decimal balance`**: Saldo total proveniente de la diferencia de ingresos y gastos.
* **`Decimal current_balance`**: Saldo actual de la cuenta
* **`previous_month()`**: Regresa al mes anterior y cambia al año anterior si es necesario. Ejecuta `load_income()`, `load_expenses()`, `load_balance()`.
* **`next_month()`**: Avanza al mes anetrior y cambia al año siguiente si es necesario. Ejecuta `load_income()`, `load_expenses()`, `load_balance()`.
* **`load_income()`**: Carga los ingresos del año y mes y los guarda en `income`.
* **`load_expenses()`**: Carga los gastos del año y mes y los guarda en `expenses`.
* **`load_balance()`**: Carga el saldo del año y el mes y los guarda en `income`.
* **`load_current_balance()`**: Carga el saldo actual de la cuenta.