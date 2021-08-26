import '../object_factory/singular_show_object.dart';


class SendODShow{
  String? show_name;
  String? current_series;
  String? current_episode;
  bool? watching;

  SendODShow({this.show_name, this.current_series, this.current_episode, this.watching});

  List<dynamic> checkValuesExist(){
    bool _is_complete = true;
    String? _missing_item;
    if (show_name == null){
      _is_complete = false;
      _missing_item = "Show Name";
    }
    else if (current_series == null){
      _is_complete = false;
      _missing_item = "Current Series";
    }
    else if (current_episode == null){
      _is_complete = false;
      _missing_item = "Current Episode";
    }

    return [_is_complete, _missing_item];
  }

  bool createNewShow(){
    final String _show_name = show_name.toString();
    //var show_object = AddOnDemandShow(name: _show_name, service: service, watching: watching, episode: episode, series: series, tags: tags)
    return true;
  }

}