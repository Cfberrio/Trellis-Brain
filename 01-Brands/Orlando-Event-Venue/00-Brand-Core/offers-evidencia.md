---
brain_note_id: "note:b5a42a10-5740-4669-82a9-072c78fb7981"
canonical_key: "00-brand-core-offers-evidencia"
brand_id: "orlando_event_venue"
---
# Offers — Evidencia

## Canonical Statement

- **fact**: In the OEV Admin panel, standard 'Discount Coupons' apply to base rental costs, while cleaning fee discounts are managed via special hardcoded logic ('Applies To: All' with a 'Cleaning fee discount' note).
- **fact**: As of June 2026, there is no visible 100% discount coupon in the production admin panel at orlandoeventvenue.org/admin/discounts.

## Evidence Log

- 2026-10-03T23:42:02.434Z — `clickup_chat_thread:8cqnrff-2077/80170035503796`
  - `e1` (source_child): No hay un nombre decidido ni un cupón de 100% visible en el Admin hoy... el encabezado indica que los “Discount Coupons” administrados allí aplican al base rent; la limpieza se maneja como especial (hardcoded)... Applies To: All y nota Cleaning fee discount (special)

- 2026-10-04T03:26:52.628Z — `clickup_chat_thread:8cqnrff-2077/80170035499061` (validation `8ae2779d-024d-4bf8-9821-c890538a5771`)
  - `e1` (source_body): hermano necesito un codigo que aplique a todo (rent y cleaning) para que nos de 100% off
- **rule**: A 100% off discount code exists or is required that applies to both base rental and cleaning fees.

- 2026-10-04T16:15:56.575Z — `clickup_chat_thread:8cqnrff-2077/80170035387402` (validation `5e9c36db-00e1-413d-9126-5427e071c7a6`)
  - `e1` (source_child): D’Loft Kitchen es el proveedor exclusivo de F&B; al confirmar la reserva, el pedido de catering se envía automáticamente al equipo de D’Loft y los fondos de F&B se enrutan a D’Loft (separados del ingreso del venue). ... no es reservable/pagable online todavía
- **process**: D’Loft Kitchen is the exclusive F&B provider for OEV; catering orders are sent automatically to their team upon booking confirmation, with F&B funds routed separately from venue revenue.
- **fact**: The 'Catering & bar — by D’Loft Kitchen' add-on is selectable during the booking flow but is not yet reservable or payable online; billing is managed directly by D’Loft.

- 2026-10-04T23:49:10.775Z — `clickup_chat_thread:8cqnrff-2077/80170035357654` (validation `1e9f702f-3c08-4da7-b83b-857e87eee830`)
  - `e1` (source_child): los entregables que debes pasar para dejar listo el entrenamiento son: Identidad oficial de la marca... Capacidad y setup (qué incluye: mesas, sillas, AV, baños, parking)... Precios/paquetes y fees (hora, día, limpieza, add‑ons)... Políticas de reserva y pago (depósito, saldo, métodos)
- **process**: Training for OEV communication agents requires specific deliverables: official brand identity, capacity and setup details (tables, chairs, AV, parking), pricing/packages (hourly, cleaning, add-ons), and booking/payment policies.

- 2026-10-04T23:53:29.553Z — `clickup_chat_thread:8cqnrff-2077/80170035306315` (validation `51ffef69-48a1-4f37-8a5b-3bd5f6c25d3e`)
  - `e1` (source_body): Como tal nos faltan el workflow de reminder, el workflow de remaining balance, hacer integración de stripe... ajustar información pequeña tipo cosas del front, precios de cleaning fee, el cobro del 20%
- **fact**: OEV operational requirements include a cleaning fee and a 20% charge as part of the pricing structure.
- **fact**: The OEV booking system requires automated workflows for reminders and remaining balance collection, integrated via Stripe.

- 2026-10-05T03:10:39.606Z — `clickup_chat_thread:8cqnrff-2077/80170035133946` (validation `4e85a4f3-521d-4871-b409-cc5c47866b63`)
  - `e1` (source_child): OEV define 50% depósito y “fully_paid” antes de in_progress... en D’Space los leads no bloquean; solo reservas con dinero (depósito/pagado/facturado) bloquean fechas
- **fact**: OEV requires a 50% deposit to secure a booking, and the status must reach 'fully_paid' before the event is considered 'in_progress'.
- **rule**: In the OEV booking system, leads do not block the calendar; only reservations with confirmed payment (deposit, paid, or invoiced) block dates.

## Provenance

- Source: `clickup_chat_thread` `8cqnrff-2077/80170035503796`
- Source hash: `1329f3ea3b4bb5597388e5730fb6e9e55cafc1a572e9bb121625ce64d9bd69aa`
- Observed at: 2026-10-03T23:42:02.434Z
- Decision: `afaf1902-a668-41bc-adc5-65502ffddd6b`
- Upstream agent run: `a5583da9-3135-4296-8be3-d10756be2cc5`
- Validation run: `b54ed0a9-5e39-481e-b7ce-e1eb27edf774`
