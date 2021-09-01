*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new group
    ${old_list}=  Get Group List
    ${group}=  New Group  name1  header1  footer1
    Create group  ${group}
    ${new_list}=  Get Group List
    append to list  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

Delete Group
    ${old_list}=  Get Group List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${group}=  get from list  ${old_list}  ${index}
    Delete Group    ${group}
    ${new_list}=    Get Group list
    remove values from list  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}
