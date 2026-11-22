-- group by, join, dan on
-- cari tren bulanan
select period, sum(amount) as total from royalties
group by period
order by period;

-- total per genre
select s.Genre, round(sum(r.amount)) as total FROM
royalties r
join songs s on s.song_id = r. song_id
group by s.genre
order by total desc

-- check jumlah lagu per genre yang mana paling besar
select genre, count(*) as jumalah_lagu
from songs
group by genre;

-- latihan
select s.genre, 
count(distinct s.song_id) as jumlah_lagu,
round(sum(r.amount)) as total,
round(sum(r.amount)) / count(distinct s.song_id) as rata_per_lagu
from royalties r
join songs s on s.song_id = r.song_id
group by s.genre
order by rata_per_lagu Desc;