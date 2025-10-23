-- LeetCode
-- 577. Employee Bonus / Easy

select name, bonus from Employee e left join Bonus b on e.empId = b.empId where bonus < 1000 or bonus is null