Feature: Contacts

  Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <firstname> and <lastname>
    When I add the contact to the list
    Then the new contact list is equal to the old list with the added contact

    Examples:
      | firstname  | lastname  |
      | firstname1 | lastname1 |
      | firstname2 | lastname2 |

  Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from the list
    Then the new contact list is equal to the old list without the deleted contact

  Scenario Outline: Modify contact
    Given a contact list
    Given a group with <name>, <header> and <footer>
    When I add the group to the list
    Then the new group list is equal to the old list with the added group

    Examples:
      | name  | header  | footer  |
      | name1 | header1 | footer1 |
      | name2 | header2 | footer2 |
