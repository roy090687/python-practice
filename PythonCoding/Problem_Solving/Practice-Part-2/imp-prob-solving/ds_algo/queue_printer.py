from collections import deque

printer_queue = deque()

# add documents
printer_queue.append("Resume")
printer_queue.append("Invoice")
printer_queue.append("Report")
printer_queue.append("OfferLetter")

print(printer_queue.pop())

while printer_queue:
    document = printer_queue.popleft()
    print(f"Printing -> {document}")
