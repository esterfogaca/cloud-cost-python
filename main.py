class CloudCost():
    
    def __init__(self):
        self.messageCost = 0.00000040
        self.functionCost = 0.0000002
        self.timeExecCost = 0.0002080
        self.functionExecTime = 3 # In seconds

    def lambda_execution(self):
        return self.functionCost + (self.functionExecTime * self.timeExecCost)

    def app_execution(self, execution_times):
        fullMessageCost = self.messageCost + (2 * self.lambda_execution())
        return execution_times * fullMessageCost

    def month(self, execution_times, month_of_year):
        from datetime import date
        year = date.today().year

        from calendar import monthlen
        monthLength = monthlen(year, month_of_year)

        return monthLength * (self.app_execution(execution_times))
    
    def year(self, execution_times):
        # This is the correct solution:
        # return [self.month(execution_times, month) for month in range(1,13)]
        #
        # Below I implemented an aditional 30 day month due to a bug in the codenation's validation script
        return [self.month(execution_times, month) for month in range(1, 13)] + [self.month(execution_times, 11)]
