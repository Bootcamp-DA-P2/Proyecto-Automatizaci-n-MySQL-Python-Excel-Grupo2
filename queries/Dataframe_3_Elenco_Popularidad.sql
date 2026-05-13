SELECT 
    f.film_id,
    f.title AS pelicula,
    CONCAT(a.first_name, ' ', a.last_name) AS actor_completo,
    COUNT(*) OVER(PARTITION BY a.actor_id) AS frecuencia_actor_total
FROM film_actor fa
JOIN film f ON fa.film_id = f.film_id
JOIN actor a ON fa.actor_id = a.actor_id
ORDER BY frecuencia_actor_total DESC, f.title;