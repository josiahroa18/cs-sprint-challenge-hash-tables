#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    starting_ticket = None
    for ticket in tickets:
        if ticket.source == "NONE":
            starting_ticket = ticket
        cache[ticket.source] = ticket.destination

    route = []
    destination = starting_ticket.destination
    while destination != 'NONE':
        route.append(destination)
        destination = cache[destination]

    route.append('NONE')

    return route
