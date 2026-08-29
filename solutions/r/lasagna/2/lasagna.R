
expected_minutes_in_oven <- function() {
  60
}

remaining_time_in_minutes <- function(time) {
  expected_minutes_in_oven() - time
}
prep_time_in_minutes <- function(layers)  {
  layers * 2
}

elapsed_time_in_minutes <- function(layers, minutes) {
  prep_time_in_minutes(layers) + minutes
}