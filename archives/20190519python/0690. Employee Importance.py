"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dict_employees={}
        for employee in employees:
            dict_employees[employee.id]=employee
            
        self.rep=0
        
        def getValOfImportance(id,dict_employees):
            self.rep+=dict_employees[id].importance
        
            for sub_id in dict_employees[id].subordinates:
                getValOfImportance(sub_id,dict_employees)
            return
        
        getValOfImportance(id,dict_employees)
        return self.rep
    
    
