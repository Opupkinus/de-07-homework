/*
 Завдання на SQL до лекції 03.
 */


/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням.
*/
select c.name
     , count(fc.film_id) as cnt_film
from film_category fc
    left join category c on fc.category_id = c.category_id
group by c.name
order by 2 desc
/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/
select a.first_name||' '||a.last_name as actor_name
    , count(r.rental_id) as cnt_rent
from actor a
    left join film_actor fa on a.actor_id = fa.actor_id
    left join film f on fa.film_id = f.film_id
    left join inventory i on f.film_id = i.film_id
    left join rental r on i.inventory_id = r.inventory_id
group by actor_name
order by 2 desc
fetch first 10 rows only
/*
3.
Вивести категорія фільмів, на яку було витрачено найбільше грошей
в прокаті
*/
select c.name
     , sum(p.amount) as spend_amount
from film_category fc
    left join category c on fc.category_id = c.category_id
    left join film f on fc.film_id = f.film_id
    left join inventory i on f.film_id = i.film_id
    left join rental r on i.inventory_id = r.inventory_id
    left join payment p on r.rental_id = p.rental_id
group by c.name
order by 2 desc
/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/
select distinct f.title
from film f
    left join inventory i on f.film_id = i.film_id
where i.film_id is null
/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/
select a.first_name||' '||a.last_name as actor_name
        , count(fc.film_id) as cnt_flm_cat
from actor a
    left join film_actor fa on a.actor_id = fa.actor_id
    left join film f on fa.film_id = f.film_id
    left join film_category fc on f.film_id = fc.film_id
    left join category c on fc.category_id = c.category_id
where c.name = 'Children'
group by actor_name
order by 2 desc
fetch first 6 rows only --оставляю ТОП 6, потому что место №3
                        --разделяют 4 актёра с одинаковым кол-вом появлений в категории
