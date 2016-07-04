{% if module_name != "Main" %}module {{module_name}} exposing (..)
{% endif %}

import Html exposing (Html, div)
import Html.App as Html

{%- if module_name == "Main" }


main = App.program
  { init = init
  , update = update
  , view = view
  , subscriptions = subscriptions
  }
{%- endif %}


-- MODEL

type alias Model =
  {
  }

init : (Model, Cmd a)
init =
  ({ mainView = Viewport.init
   , currentFunc = Piecewise.initial (vec2 0 0) (vec2 25 1000)
   }, Cmd.none)


-- UPDATE

type Msg = NoMsg
         | NoMsg2

update : Msg -> Model -> (Model, Cmd a)
update msg model = (model, Cmd.none)


-- SUBSCRIPTIONS

subscriptions : Model -> Sub Msg
subscriptions model =
  Sub.none


-- VIEW

view : Model -> Html Msg
view model = div []
  [ ]
