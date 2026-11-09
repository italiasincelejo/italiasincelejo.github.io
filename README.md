# Arma tu pizza · Italia Sincelejo 🍕

Página web interactiva para que los clientes de **Italia** (comidas rápidas, Plaza Cultural de Majagual, Sincelejo) armen su pizza personal de 27 cm, la vean salir del horno en 3D y envíen el pedido por WhatsApp.

## ¿Qué hace?

- **Armar la pizza:** la base (salsa de tomate de la casa, mozzarella y finas hierbas) va incluida. Luego, el cliente agrega las adiciones que quiera y puede pedir doble porción de cada una.
- **Precio en vivo:** el total cambia con cada ingrediente.
- **Pedido de varias pizzas:** cada pizza horneada entra al pedido. Desde el botón **Mi pedido**, el cliente puede cambiar la cantidad, editar o quitar cualquier pizza.
- **Envío por WhatsApp:** al finalizar, se abre WhatsApp con el pedido ya escrito: cada pizza, sus adiciones, los subtotales, el total, el nombre, la dirección y las notas del cliente.
- **Funciona en celular y en computador:** en celular, la pantalla queda fija, con una bandeja de ingredientes por pestañas.
- **Bienvenida con Niko:** la mascota de Italia recibe al cliente con una pantalla animada y lo acompaña mientras arma su pizza.
- **Modo restaurante (kiosco):** al agregar `#kiosco` al final del enlace, la página muestra una pantalla de bienvenida y se reinicia sola después de 90 segundos sin uso.

## Dirección de la página

- Página: **https://italiasincelejo.github.io/**
- Tablet del restaurante (modo kiosco): **https://italiasincelejo.github.io/#kiosco**
- Código QR para imprimir: `assets/qr-italiasincelejo.png`

GitHub Pages publica automáticamente cada cambio que se sube a la rama `main`.
El enlace anterior (`einerjoseperez2021-debug.github.io/italia-arma-tu-pizza/`) redirige a esta dirección.

## Cómo cambiar precios o datos

Todo lo que se ajusta con frecuencia está al inicio del código, en `index.html`, en la sección **CONFIGURACIÓN**:

```js
const WHATSAPP = '573122957109';   // número que recibe los pedidos (con el 57 de Colombia)
const PRECIO_BASE = 11500;         // pizza base: tomate, mozzarella y finas hierbas
const PRECIO_CATEGORIA = { proteina: 2000, vegetal: 1000, fruta: 1500, queso: 2000, premium: 4000, salsa: 1000 };
const GOATCOUNTER_CODIGO = 'italia-sincelejo'; // panel: https://italia-sincelejo.goatcounter.com
const POSTHOG_CLAVE = 'phc_...';   // clave pública del proyecto de PostHog (solo envía datos)
const KIOSCO_INACTIVIDAD_SEG = 90; // segundos sin uso antes de reiniciar en modo kiosco
```

Los ingredientes están en la lista `TOPS`, donde a cada uno se le asigna su categoría de precio.

> **Nota:** los precios de las adiciones son **provisionales**. Salen del análisis de la carta actual y se van a ajustar con el estudio de costos por ingrediente (archivo de Excel del proyecto).

## Medir resultados

La página envía datos anónimos de uso a dos servicios gratuitos:

- **PostHog** (análisis completo): panel **"Italia · Arma tu pizza"** en `https://us.posthog.com`, con el embudo de conversión, los ingredientes más pedidos, las ventas estimadas, el ticket promedio, los dispositivos, la hora con más pedidos y las grabaciones de sesión.
- **GoatCounter** (conteo simple, respaldo): `https://italia-sincelejo.goatcounter.com`

Eventos que se registran en PostHog:

| Evento | Cuándo ocurre |
|---|---|
| `bienvenida_vista` / `bienvenida_completada` | Se muestra y se pasa la bienvenida de Niko |
| `base_completa` | El cliente pone salsa y queso |
| `ingrediente_agregado` | Cada adición (nombre, categoría, precio, porción) |
| `pizza_horneada` | La pizza se manda al horno (ingredientes y precio) |
| `resumen_pedido_visto` | Se ve el resumen del pedido |
| `pedido_enviado` | Se envía el pedido por WhatsApp (pizzas, total, ingredientes) |
| `cantidad_aumentada`, `pizza_editada`, `pizza_quitada`, `otra_pizza`, `deshacer`, `formulario_incompleto` | Uso del pedido y señales de dificultad |

**Para hacer pruebas sin dañar las estadísticas,** abre la página con `?prueba=1` al final del enlace. Esas visitas se excluyen del panel.

**Privacidad:** el nombre, la dirección y las notas nunca se envían a PostHog ni a GoatCounter. Los campos del formulario y el botón de WhatsApp están bloqueados en las grabaciones, y el enlace de WhatsApp solo se arma en el momento del clic.

## Imagen de vista previa

Cuando alguien comparte el enlace por WhatsApp, Facebook o Instagram, aparece una tarjeta con título, descripción e imagen. El título y la descripción ya están listos. La imagen es `og-image.png`, con Niko y el mensaje principal. En la carpeta `assets` está el código QR listo para imprimir.

## Privacidad

La página no tiene servidor ni base de datos. Cada persona arma su pedido en su propio dispositivo, y los datos (nombre, dirección y notas) solo se usan para escribir el mensaje de WhatsApp. En un celular personal, el nombre y la dirección quedan guardados únicamente en ese navegador para el siguiente pedido. En modo kiosco no se guarda nada.

## Créditos

Proyecto de Marketing y Negocios Digitales · TEINCO.
Hecho para **Italia**, Sincelejo · [@italiasincelejo](https://www.instagram.com/italiasincelejo/)
