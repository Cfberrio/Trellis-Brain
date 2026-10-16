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

- 2026-10-09T18:30:48.478Z — `clickup:86e32c6h7` (validation `bf9370bb-05b4-46e8-8083-0f3545a44cf6`)
  - `e1` (source_child): estoy pensando en cambiar el flujo a que hagan el booking con $100 non refundable + un step donde escanean su licencia al final (proteccion legal)
  - `e2` (source_child): For $899 you get 24hr access to our venue included with 90 chairs, 10 tables... Hourly rentals are also available for $140/hour... Book online with 50% of total amount and the balance is due 15 days before your event
- **decision**: The booking flow is being updated to include a $100 non-refundable deposit option for leads with budget constraints, followed by a legal protection step requiring a license scan.
- **fact**: Standard booking terms require a 50% deposit of the total amount at the time of booking, with the remaining balance due 15 days before the event.
- **fact**: The 24-hour venue access package is priced at $899 and includes 90 chairs, 10 tables, prep kitchen, and parking. Hourly rentals are available at $140/hour.

- 2026-10-16T16:58:54.664Z — `clickup_doc_page:8cqnrff-18077/8cqnrff-22497` (validation `59a87dd5-dc01-4390-a58a-013dd269db19`)
  - `e1` (source_body): The team decided to enforce venue policies rigorously, including a strict no‐alcohol rule unless managed by approved vendors... requiring use of approved vendors for beer and wine due to nonprofit constraints.
  - `e2` (source_body): Discount code setup was illustrated through the creation of codes (e.g., GRAD20) and adjustments to percentages or fixed amounts to attract and manage customer reservations.
  - `e3` (source_body): demonstrating how bookings are differentiated by type (hourly vs. all-day)... syncing internal events with customer bookings, and ensuring updates appear in both systems.
- **rule**: OEV enforces a strict no-alcohol policy unless managed by approved vendors for beer and wine, primarily due to non-profit constraints.
- **fact**: Discount codes (e.g., GRAD20) are used to manage customer reservations, with adjustments possible for percentages or fixed amounts.
- **process**: Venue bookings are differentiated by type (hourly vs. all-day) and managed via a centralized calendar that syncs internal events with customer bookings.

- 2026-10-16T16:59:31.876Z — `clickup_doc_page:8cqnrff-18077/8cqnrff-22537` (validation `89abfb5e-7a98-4b76-ad8f-3e7216779c06`)
  - `e1` (source_body): Hourly rental: $139/hour. Minimum booking: 4 hours. Full-day special: $899. Included: 90 chairs and tables, prep kitchen, two bathrooms, main venue space.
  - `e2` (source_body): Outside alcohol should not be allowed unless managed through the approved vendor/staff process. The transcript explains that beer/wine must be served through the approved vendor because of venue/nonprofit rules.
  - `e3` (source_body): Basic offer can be around $100 off. Multi-day or larger bookings may receive up to 20% off. Do not exceed 20%.
- **rule**: Standard venue rental pricing is $139/hour with a 4-hour minimum booking requirement.
- **rule**: A full-day venue rental special is available for $899.
- **rule**: Outside alcohol is strictly prohibited; beer and wine must be served through the approved vendor/staff process due to venue and nonprofit compliance rules.
- **rule**: Standard closing incentives are typically $100 off; multi-day or large bookings may receive up to 20% off, but discounts should not exceed 20% without escalation.
- **fact**: Base rental includes 90 chairs and tables, a prep kitchen, two bathrooms, and the main venue space.

- 2026-10-16T17:00:16.747Z — `clickup_doc_page:8cqnrff-18077/8cqnrff-22557` (validation `a861aff9-742d-4111-8bb0-5e39fced1618`)
  - `e1` (source_body): Hourly: $139/hour. Minimum: 4 hours. Full day: $899.
  - `e2` (source_body): Beer/wine can only be served through the approved vendor/staff process. Outside alcohol is not allowed. Non-alcoholic drinks like water and soda are okay.
  - `e3` (source_body): Simple discount: around $100 off. Larger/multi-day bookings: up to 20%. Do not go above 20% without Luis.
- **rule**: Hourly rental is $139/hour with a 4-hour minimum booking requirement.
- **rule**: Outside alcohol is prohibited; beer and wine may only be served through OEV's approved vendor/staff process.
- **rule**: Standard discounts include approximately $100 off as a closing incentive, with larger or multi-day bookings eligible for up to 20% off (management approval required above 20%).

## Provenance

- Source: `clickup_chat_thread` `8cqnrff-2077/80170035503796`
- Source hash: `1329f3ea3b4bb5597388e5730fb6e9e55cafc1a572e9bb121625ce64d9bd69aa`
- Observed at: 2026-10-03T23:42:02.434Z
- Decision: `afaf1902-a668-41bc-adc5-65502ffddd6b`
- Upstream agent run: `a5583da9-3135-4296-8be3-d10756be2cc5`
- Validation run: `b54ed0a9-5e39-481e-b7ce-e1eb27edf774`
