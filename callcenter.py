class call(object):
    def __init__(self, unique_id, caller_name, caller_phone, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call

    def display_attributes(self):
        print "Caller's unique id:", self.unique_id
        print "Caller's name:", self.caller_name
        print "Caller's phone number:", self.caller_phone
        print "Time of call:", self.time_of_call
        print "Reason for call:", self.reason_for_call

    def name_number(self):
        print self.caller_name, self.caller_phone

    def phone_number(self):
        return self.caller_phone

class callcenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add_call(self, new_call):
        self.calls.append(new_call)
        self.queue_size = len(self.calls)

    #remove call with specified caller number, or the first in the queue if no number is supplied
    def remove(self, caller_phone = -1):
        if caller_phone > -1:
            for num in range(0, len(self.calls)):
               if caller_phone == self.calls[num].phone_number():
                    old_call = self.calls.pop(num)
                    break
        else:
            old_call = self.calls.pop(0)
        self.queue_size = len(self.calls)
        return(old_call)

    def info(self):
        for val in self.calls:
            val.name_number()
        print "Queue size:", self.queue_size



c1 = call(1, "Betty Ford", 2539512453, "9:02", "purchace")
c2 = call(2, "John Glenn", 2064329641, "11:43", "purchace")
c3 = call(3, "Frank Limb", 3608542193, "12:21", "return")

cc1 = callcenter()
cc1.add_call(c1)
cc1.add_call(c2)
cc1.add_call(c3)
cc1.info()
cc1.remove(2064329641)
cc1.info()