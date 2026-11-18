-- select * from songs limit 10;
-- select count(*) from royalties;

-- total per source
-- select source, sum(amount) as total
-- from royalties
-- group by source
-- order by  total DESC

-- top 10 lagu berdasarkan total royalties
select s.title, s.writer, sum(r.amount) as total FROM royalties r
Join songs s on s.song_id = r.song_id
group by s.song_id
order by total DESC
limit 10;

-- tren bulanan
select period, sum(amount) as total
from royalties
group by period
order by period	

-- total genre
select s.genre, round(sum(r.amount)) as total
from royalties r
join songs s on s.song_id = r.song_id
group by s.genre
order by total DESC

-- total royalty per bulan untuk genre dangdut
select s.genre, r.period, round(sum(r.amount)) as total
from royalties r
join songs s on s.song_id = r.song_id
where s.genre is "Dangdut"
group by r.period
order by total desc