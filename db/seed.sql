-- SQLite seed for demo
INSERT INTO suppliers(name, contact_info) VALUES
 ('ACME Ltd', 'acme@example.com'),
 ('Bolt & Nut', 'sales@bn.com');

INSERT INTO components(name, unit, quantity_in_stock) VALUES
 ('Screw M3', 'pcs', 500),
 ('Nut M3',   'pcs', 800);

-- Simulate one expense
UPDATE components SET quantity_in_stock = quantity_in_stock - 100 WHERE name='Screw M3';
INSERT INTO supply_history(supplier_id, component_id, qty, date)
VALUES (1, 1, 100, datetime('now'));
