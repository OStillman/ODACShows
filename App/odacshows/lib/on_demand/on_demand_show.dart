import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import '/helpers/constants.dart';
import 'object_factory/on_demand_show.dart';
import '/on_demand/on_demand_show.dart';
import '/helpers/constants.dart';

class OnDemandShow_UI extends StatefulWidget {
  final String show_name;
  final String show_id;

  const OnDemandShow_UI(this.show_name, this.show_id);

  @override
  _OnDemandShow_UI createState() => _OnDemandShow_UI();
}

class _OnDemandShow_UI extends State<OnDemandShow_UI> {
  late Future<OnDemandShow> _futureODShows;

  Future<OnDemandShow> fetchODShows() async {
    OnDemandShow onDemandShows;
    String show_id = widget.show_id;
    final response =
        await http.get(Uri.parse('$base_url/ODAC/shows/api/od?show=$show_id'));
    if (response.statusCode == 200) {
      print("Request Succeeded");
      //print(response.body);
      var onDemandShowsJSON = json.decode(response.body);
      onDemandShows = OnDemandShow.fromJson(onDemandShowsJSON);
      return onDemandShows;
      //return OnDemandShows.fromJson(jsonDecode(response.body));
    } else {
      throw Exception('Failed to load On Demand Shows');
    }
  }

  @override
  void initState() {
    super.initState();
    _futureODShows = fetchODShows();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey[800],
      appBar: AppBar(
        title: Text(widget.show_name),
      ),
      body: FutureBuilder<OnDemandShow>(
        future: _futureODShows,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            var data = snapshot.data;
            if (data != null) {
              return OutputOD(data.odShow);
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
    );
  }

  Widget OutputOD(all_od_shows) {
    if (all_od_shows.length == 0) {
      return NoShows();
    } else {
      return ShowOutput(all_od_shows);
    }
  }

  Widget ShowOutput(shows) {
    Widget output_card = NoShows();
    for (var show in shows) {
      output_card = Card(
          child: Column(
        mainAxisSize: MainAxisSize.min,
        children: <Widget>[
          ListTile(
            title: Text(show.name),
            subtitle: WatchingStatus(show.watching),
            trailing: Icon(Icons.edit),
          ),
          DataTable(dividerThickness: 0, columns: const <DataColumn>[
            DataColumn(label: Text("Element")),
            DataColumn(label: Text("Detail")),
            DataColumn(label: Text("Edit")),
          ], rows: <DataRow>[
            Service(show.service),
            Series(show.series),
            Episode(show.episode),
          ]),
          ToggleWatching(show.watching),
        ],
      ));
    }
    return output_card;
  }

  Widget WatchingStatus(status) {
    if (status == "N") {
      return Text("You ARE NOT watching this show");
    } else {
      return Text("You ARE watching this show");
    }
  }

  DataRow Service(service) {
    //TODO: Run a Service Query - This currently gives Service number
    return DataRow(cells: <DataCell>[
      DataCell(Text("Service")),
      DataCell(Text("BBC")),
      DataCell(GestureDetector(
        onTap: () {
          print("edit selected");
        },
        child: Icon(Icons.edit),
      )),
    ]);
  }

  DataRow Series(series) {
    return DataRow(cells: <DataCell>[
      DataCell(Text("Series")),
      DataCell(Text(series.toString())),
      DataCell(GestureDetector(
        onTap: () {
          print("edit selected");
        },
        child: Icon(Icons.edit),
      )),
    ]);
  }

  DataRow Episode(episode) {
    return DataRow(cells: <DataCell>[
      DataCell(Text("Episode")),
      DataCell(Text(episode.toString())),
      DataCell(GestureDetector(
        onTap: () {
          print("edit selected");
        },
        child: Icon(Icons.edit),
      )),
    ]);
  }

  Widget ToggleWatching(status){
    if (status == "Y"){
      return Row(
        mainAxisAlignment: MainAxisAlignment.end,
        children: <Widget>[
          GestureDetector(
              onTap: (){
                print("Toggle Watching Tapped");
              },
              child:Icon(Icons.bookmark_border_outlined)
          ),
        ],
      );
    }
    else{
      return Row(
        mainAxisAlignment: MainAxisAlignment.end,
        children: <Widget>[
          GestureDetector(
              onTap: (){
                print("Toggle Watching Tapped");
              },
              child:Icon(Icons.bookmark_add_outlined)
          ),
        ],
      );
    }
  }

  Widget NoShows() {
    return Center(
      child: Container(
          padding: const EdgeInsets.all(8),
          width: MediaQuery.of(context).size.width,
          color: Colors.cyan[800],
          child: Text("Something went wrong, We can't find that On Demand Show",
              textAlign: TextAlign.center)),
    );
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
}
