// To parse this JSON data, do
//
//     final onDemandShows = onDemandShowsFromJson(jsonString);

import 'package:meta/meta.dart';
import 'dart:convert';

class OnDemandShows {
  OnDemandShows({
    required this.odShows,
  });

  List<OdShow> odShows;

  factory OnDemandShows.fromRawJson(String str) => OnDemandShows.fromJson(json.decode(str));

  String toRawJson() => json.encode(toJson());

  factory OnDemandShows.fromJson(Map<String, dynamic> json) => OnDemandShows(
    odShows: List<OdShow>.from(json["od_shows"].map((x) => OdShow.fromJson(x))),
  );

  Map<String, dynamic> toJson() => {
    "od_shows": List<dynamic>.from(odShows.map((x) => x.toJson())),
  };
}

class OdShow {
  OdShow({
    required this.episode,
    required this.id,
    required this.name,
    required this.series,
    required this.service,
    required this.watching,
  });

  int episode;
  int id;
  String name;
  int series;
  String service;
  String watching;

  factory OdShow.fromRawJson(String str) => OdShow.fromJson(json.decode(str));

  String toRawJson() => json.encode(toJson());

  factory OdShow.fromJson(Map<String, dynamic> json) => OdShow(
    episode: json["episode"],
    id: json["id"],
    name: json["name"],
    series: json["series"],
    service: json["service"],
    watching: json["watching"],
  );

  Map<String, dynamic> toJson() => {
    "episode": episode,
    "id": id,
    "name": name,
    "series": series,
    "service": service,
    "watching": watching,
  };
}
