INSERT INTO suppliers(name, contact) VALUES
    ('ACME Ltd', 'acme@example.com'),
    ('Bolt & Nut', 'sales@bn.com');

INSERT INTO components(name, unit, quantity_in_stock) VALUES
    ('Screw M3', 'pcs', 500),
    ('Nut M3', 'pcs', 800),
    ('Bolt M5', 'pcs', 300);

INSERT INTO supply_history(supplier_id, component_id, qty, date)
VALUES (1, 1, 200, datetime('now','-2 days'));
