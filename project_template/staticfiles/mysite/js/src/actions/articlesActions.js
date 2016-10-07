import { request } from "../utils"

export const FETCH_ARTICLES = "FETCH_ARTICLES"
export const FETCH_ARTICLES_SUCCESS = "FETCH_ARTICLES_SUCCESS"
export const FETCH_ARTICLES_ERROR400 = "FETCH_ARTICLES_ERROR400"
export const FETCH_ARTICLES_ERROR500 = "FETCH_ARTICLES_ERROR500"
export const FETCH_ARTICLES_FAILURE = "FETCH_ARTICLES_FAILURE"
export function fetchRepos() {
  return function (dispatch) {
    let url = "/api/articles/"
    dispatch({type: FETCH_ARTICLES})
    return request(
      url, {},
      (json) => { dispatch({type: FETCH_ARTICLES_SUCCESS, res: json}) },
      (json) => { dispatch({type: FETCH_ARTICLES_ERROR400, res: json}) },
      (res) => { dispatch({type: FETCH_ARTICLES_ERROR500, res: res}) },
      (ex) => { dispatch({type: FETCH_ARTICLES_FAILURE, error: ex}) },
    )
  }
}