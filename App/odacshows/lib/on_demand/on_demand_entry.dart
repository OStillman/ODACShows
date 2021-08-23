import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:odacshows/on_demand/on_demand_show.dart';

import '/helpers/constants.dart';
import 'object_factory/on_demand_shows.dart';
import '/on_demand/on_demand_show.dart';

class OnDemandEntry extends StatefulWidget {
  @override
  _OnDemandEntry createState() => _OnDemandEntry();
}

class _OnDemandEntry extends State<OnDemandEntry> {
  late Future<OnDemandShows> futureODShows;

  Future<OnDemandShows> fetchODShows() async {
    OnDemandShows onDemandShows;
    final response = await http.get(Uri.parse('$base_url/ODAC/shows/api/od'));
    if (response.statusCode == 200) {
      print("Request Succeeded");
      //print(response.body);
      var onDemandShowsJSON = json.decode(response.body);
      onDemandShows = OnDemandShows.fromJson(onDemandShowsJSON);
      return onDemandShows;
      //return OnDemandShows.fromJson(jsonDecode(response.body));
    } else {
      throw Exception('Failed to load On Demand Shows');
    }
  }

  void _incrementCounter() {
    setState(() {});
  }

  @override
  void initState() {
    super.initState();
    futureODShows = fetchODShows();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey[800],
      appBar: AppBar(
        title: Text("On Demand Shows"),
      ),
      body: FutureBuilder<OnDemandShows>(
        future: futureODShows,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            var data = snapshot.data;
            if (data != null) {
              return OutputOD(data.odShows);
              //return Text("Works");
            } else {
              return Text("No Shows?!");
            }
          } else if (snapshot.hasError) {
            return Text('${snapshot.error}');
          }

          // By default, show a loading spinner.
          return DefaultLoading();
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        child: const Icon(Icons.add),
      ),
    );
  }

  Widget OutputOD(all_od_shows) {
    if (all_od_shows.length == 0) {
      return NoShows();
    } else {
      return GridView.count(
          crossAxisCount: 3,
          mainAxisSpacing: 10,
          crossAxisSpacing: 10,
          padding: const EdgeInsets.all(20),
          children: FormatODShows(all_od_shows));
    }
  }

  List<Widget> FormatODShows(all_od_shows) {
    List<Widget> all_widgets = [];
    for (var show in all_od_shows) {
      Widget this_widget;
      String progress;
      String show_name = show.name;
      String watching = show.watching;

      if (show.episode == 0 && show.series == 0) {
        progress = "";
      } else {
        String episode = show.episode.toString();
        String series = show.series.toString();
        progress = "S$series, Ep$episode";
      }

      if (watching == "Y") {
        this_widget = Container(
            padding: const EdgeInsets.all(8),
            color: Colors.cyan[800],
            child: GestureDetector(
              onTap: () {
                String show_id = show.id.toString();
                Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) =>
                            OnDemandShow_UI(show_name, show_id)));
              },
              child: Container(
                  padding: const EdgeInsets.all(8),
                  color: Colors.cyan[800],
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      Text("$show_name", style: TextStyle(color: Colors.white)),
                      Spacer(),
                      Text(
                        progress,
                        style: TextStyle(
                            fontWeight: FontWeight.w100, color: Colors.white),
                      )
                    ],
                  )),
            ));
      } else {
        this_widget = Opacity(
          opacity: 0.4,
          child: GestureDetector(
            onTap: () {
              String show_id = show.id.toString();
              Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => OnDemandShow_UI(show_name, show_id)));
            },
            child: Container(
                padding: const EdgeInsets.all(8),
                color: Colors.cyan[800],
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Text("$show_name", style: TextStyle(color: Colors.white)),
                    Spacer(),
                    Text(
                      progress,
                      style: TextStyle(
                          fontWeight: FontWeight.w100, color: Colors.white),
                    )
                  ],
                )),
          ),
        );
      }

      all_widgets.add(this_widget);
    }

    return all_widgets;
  }

  Widget DefaultLoading() {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          CircularProgressIndicator(
            color: Colors.cyan,
          ),
          Padding(
            padding: EdgeInsets.only(top: 30),
            child: Text(
              "Loading, Please Wait...",
              style: TextStyle(color: Colors.white),
            ),
          ),
        ],
      ),
    );
  }

  Widget AddButton() {
    return FloatingActionButton(
      onPressed: () {},
      child: const Icon(Icons.add),
    );
  }

  Widget NoShows() {
    return Center(
      child: Container(
          padding: const EdgeInsets.all(8),
          width: MediaQuery.of(context).size.width,
          color: Colors.cyan[800],
          child:
              Text("You Have No On Demand Shows", textAlign: TextAlign.center)),
    );
  }

/*@override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey[800],
      appBar: AppBar(
        title: Text("On Demand Shows"),
      ),
      body: GridView.count(
        crossAxisCount: 3,
        mainAxisSpacing: 10,
        crossAxisSpacing: 10,
        padding: const EdgeInsets.all(20),
        children: <Widget>[
          Container(
              padding: const EdgeInsets.all(8),
              color: Colors.cyan[800],
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[Text("Test Show", style: TextStyle(color: Colors.white)), Spacer(), Text("S1, Ep24", style: TextStyle(fontWeight: FontWeight.w100, color: Colors.white),)],
              )),
          Container(
              padding: const EdgeInsets.all(8),
              color: Colors.cyan[800],
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[Text("Test Show", style: TextStyle(color: Colors.white)), Spacer(), Text("S5, Ep12", style: TextStyle(fontWeight: FontWeight.w100, color: Colors.white),)],
              )),
          Opacity(
              opacity: 0.4,
              child: Container(
                  padding: const EdgeInsets.all(8),
                  color: Colors.cyan[800],
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[Text("Test Show", style: TextStyle(color: Colors.white)), Spacer(),],
                  )),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: (){},
        child: const Icon(Icons.add),
      ),
    );
  }*/
}
