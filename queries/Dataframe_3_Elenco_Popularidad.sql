USE sakila;

SELECT
    f.film_id,
    f.title AS Pelicula,
    f.release_year AS Año_lanzamiento,
    c.name AS Categoria,
    l.name AS Idioma,
    f.rating AS Clasificacion,
    COUNT(DISTINCT i.inventory_id) AS Copias_en_inventario
FROM film f
INNER JOIN film_category fc ON f.film_id = fc.film_id
INNER JOIN category c ON fc.category_id = c.category_id
INNER JOIN language l ON f.language_id = l.language_id
LEFT JOIN inventory i ON f.film_id = i.film_id
GROUP BY f.film_id, f.title, f.release_year, c.name, l.name, f.rating;