-- LeetCode
-- 1378. Replace Employee ID With The Unique Identifier / Easy

select eu.unique_id as unique_id,
    e.name as name
from Employees e
left join EmployeeUNI eu on e.id = eu.id
