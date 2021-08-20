import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import '/helpers/constants.dart';
import 'object_factory/on_demand_shows.dart';

class OnDemandEntry extends StatefulWidget {
  @override
  _OnDemandEntry createState() => _OnDemandEntry();
}

class _OnDemandEntry extends State<OnDemandEntry> {
  late Future<OnDemandShows> futureODShows;
  Future<OnDemandShows> fetchODShows() async{
    OnDemandShows onDemandShows;
    final response = await http.get(Uri.parse('http://192.168.68.139:5000/ODAC/shows/api/od'));
    if (response.statusCode == 200){
      print("Request Succeeded");
      //print(response.body);
      var onDemandShowsJSON = json.decode(response.body);
      onDemandShows = OnDemandShows.fromJson(onDemandShowsJSON);
      return onDemandShows;
      //return OnDemandShows.fromJson(jsonDecode(response.body));
    }
    else{
      throw Exception('Failed to load On Demand Shows');
    }
  }


  void _incrementCounter() {
    setState(() {});
  }

  @override
  void initState(){
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
          builder: (context, snapshot){
            if (snapshot.hasData) {
              print(snapshot.data);
              var data = snapshot.data;
              if (data != null){
                print(data.odShows[0].id);
              }
              return Text("Works");
            } else if (snapshot.hasError) {
              return Text('${snapshot.error}');
            }

            // By default, show a loading spinner.
            return const CircularProgressIndicator();
          },
        )
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
