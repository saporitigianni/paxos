.. -*-restructuredtext-*-

Usage
-----

Note: Sample test cases are provided in the under each folder
Run using **python3 script_name args** or use **chmod +x script_name** and then **./script_name args** (might have to modify shebang line)

**Question 1:** For bottleneck explanation see `main.py <https://github.com/saporitigianni/flaskapp/blob/master/main.py>`_
**For more sourcecode see separate `repo <https://github.com/saporitigianni/flaskapp>`_**

.. code:: python

    $ curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' https://omega-palace-205901.appspot.com/messages
    {
    "digest": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
    }

    $ curl https://omega-palace-205901.appspot.com/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae
    {
    "message": "foo"
    }

    $ curl -i https://omega-palace-205901.appspot.com/messages/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    HTTP/1.1 404 Not Found
    Content-Type: text/html; charset=utf-8
    X-Cloud-Trace-Context: 01e077281b0eda2aaaf64b56e2df14b2;o=1
    Date: Sat, 07 Jul 2018 20:43:06 GMT
    Server: Google Frontend
    Content-Length: 39
    Alt-Svc: quic=":443"; ma=2592000; v="43,42,41,39,35"

    {
        "err_msg": "Message not found"
    }

**Question 2:** For Big O explanation see `giftcard_spending.py <https://github.com/saporitigianni/paxos/blob/master/giftcard_spending/giftcard_spending.py>`_

.. code:: python

    # Navigate to /giftcard_spending and execute
    $ python3 giftcard_spending.py prices.txt 2500
    Candy Bar 500, Earmuffs 2000

    # or run test cases
    $ python3 test_giftcard_spending.py

**Question 3:** For Big O explanation see `wildcard_combinations.py <https://github.com/saporitigianni/paxos/blob/master/wildcard_combinations/wildcard_combinations.py>`_

.. code:: bash

    # Navigate to /wildcard_combinations and execute
    $ python3 wildcard_combinations.py 10X10X

    101101
    100101
    101100
    100100

    # or run test cases
    $ python3 test_wildcard_combinations.py
