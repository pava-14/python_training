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
    Given a non-empty contact list
    Given a random contact from the list
    Given a new contact data with <firstname> and <lastname>
    When I modify a contact from a list with a new contact data
    Then the new contact list is equal to the old list with modified contact

    Examples:
      | firstname   | lastname   |
      | firstname14 | lastname14 |
      | firstname15 | lastname15 |
