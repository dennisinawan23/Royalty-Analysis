-- select * from songs
-- limit 3;
-- 
-- select * from royalties limit 5;

-- top 10 lagu berdasarkan royalty
-- select s.title, s.writer, sum(r.amount) as total FROM
-- royalties r
-- join songs s on s.song_id = r.song_id
-- group by s.song_id
-- order by total DESC
-- limit 10;

select sum(amount) from royalties;

select sum(r.amount) from royalties r
join songs s on s.song_id = r.song_id;

select count(*)
from royalties r
join songs s;

select title, count(*) as jumlah
where songs
group by title
having count(*) > 1;\


select DISTINCT period from 
royalties
order by period;
