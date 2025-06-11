INSERT INTO suppliers(name, contact_info) VALUES
 ('ACME Ltd','acme@mail.com'),
 ('Bolt & Nut','sales@bn.com');

INSERT INTO components(name, unit, quantity_in_stock) VALUES
 ('Screw M3','pcs',500),
 ('Nut M3','pcs',800),
 ('Bolt M5','pcs',300);

-- add one supply record to history
INSERT INTO supply_history(supplier_id, component_id, qty, date)
VALUES (1, 1, 200, datetime('now','-2 days'));
