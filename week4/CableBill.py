# Declare some constants
R_PROCESS_FEE    = 4.5
R_SERVICE_FEE    = 20.5
R_CHANNEL_FEE    = 7.5

B_PROCESS_FEE    = 15.0
B_SERVICE_FEE    = 75.0
B_ADDITIONAL_FEE = 5.0
B_CHANNEL_FEE    = 50.0


account_no = int(input('Enter account number: '))
customer_code = input('Enter customer code (R/B): ')
n_channels = int(input('Enter number of channels: '))


is_residentCode = customer_code.lower() == 'r'
is_businessCode = customer_code.lower() == 'b'
if not (is_residentCode or is_businessCode):
    print('Invalid customer code!')
    exit()


billAmount = 0
if is_residentCode:
    billAmount = R_PROCESS_FEE + R_SERVICE_FEE + n_channels * R_CHANNEL_FEE
else:
    nConnections = int(input('Enter number of connections: '))
    additionalFee = 0 if nConnections < 11 else B_ADDITIONAL_FEE * (nConnections - 10)
    billAmount = B_PROCESS_FEE + B_SERVICE_FEE + additionalFee + n_channels * B_CHANNEL_FEE


# Calculate bill Amount
# Print account number, customer type, number of channels, bill amount if resident
# Print account number, customer type, number of channels, number of connections, bill amount if business
print('+' + '-' * 20 + '+' + '-' * 10 + '+')
print('|{:<20}|{:>10}|'.format('Account Number', account_no))
print('|{:<20}|{:>10}|'.format('Customer Type', 'Resident' if is_residentCode else 'Business'))
print('|{:<20}|{:>10}|'.format('No Channels', n_channels))
if is_businessCode:
    print('|{:<20}|{:>10}|'.format('No Connections', nConnections))
print('|{:<20}|{:>10.2f}|'.format('Bill Amount', billAmount))
print('+' + '-' * 20 + '+' + '-' * 10 + '+')




