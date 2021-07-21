ODAC Shows - Backend\AllShows.py
================================

All Shows controls the output of all the current shows saved in the database. Both On Demand (ODShows) and Live Shows will can be pulled from this file.

References
----------

This file is referenced during the following operations:

- On Navigation to the index Page (Function: Index, File: endpoint_control.py)

GetAllLiveShows
---------------

From the Database (referencing the LiveShows table) this Class will pull the records into a JSON formatted output with the following template:

.. code-block:: JSON

    {
        "Planner" {
            Shows {[
                "id": xxx,
                "name": xxx,
                "channel": xxx,
                "series": xxx,
                "episode": xxx
            ]}
        }
    }
   
   

GetAllODShows
--------------

Similar logic is used with the On Demand Shows Class (GetAllODShows). 

Initally, it fetches the On Demand shows by calling the ODShows table. 

This, much like above, will then be formatted into appropriate JSON using the following template:

.. code-block:: JSON

    {
        "Planner" {
            Shows {[
                "id": xxx,
                "name": xxx,
                "watching": Y/N,
                "channel": xxx,
                "series": xxx,
                "episode": xxx
                "tags": [xx,xx,xx]
            ]}
        }
    }
    
    
Note the diffrences here include:

- Watching - A Y/N attribute which the user can define at the frontend to mark if they are actively watching this on demand show, or if they haven't started/may have finished/are no longer watching a certain show. The idea is for users to be able to add many On Demand shows and only mark a small subset of them as currently in progress, leaving the rest off. The user may also turn the watching to N if they are waiting for the next series. 
- Tags - Each OD show is referenced with a tag, these tags are user defined. They can be used in the UI for the user to select a show of a certain type i.e. Drama, Comedy etc. that they may be interested in watching

In order for the tags to be fetched, a middle table is used. This table will contain the ID of the On Demand show and the ID of the linked Tag. I.e. One On Demand Show can have Many Tags

During each On Demand show read, the related tags will be fetched using a database query of the middle table, with a join to the outer Tag table