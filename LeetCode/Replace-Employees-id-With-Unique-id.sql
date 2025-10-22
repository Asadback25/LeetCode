-- LeetCode
-- 1378. Replace Employees ID With Unique ID / Easy

select eu.unique_id as unique_id, e.name as name from Employees e left join EmployeeUNI eu on e.id = eu.id