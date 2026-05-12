
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    f.film_id,
    f.title,
    SUM(p.amount) AS total_pagado,
    COUNT(p.payment_id) AS total_alquileres
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
GROUP BY c.customer_id, c.first_name, c.last_name, f.film_id, f.title
ORDER BY total_pagado DESC;