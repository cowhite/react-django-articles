import * as githubActions from "../actions/articlesActions"

const initialState = {
  isLoadingRepos: false,
  repos: undefined,
}

export default function articles(state=initialState, action={}) {
  switch (action.type) {
  case githubActions.FETCH_ARTICLES:
    return {...state, isLoadingRepos: true}
  case githubActions.FETCH_ARTICLES_SUCCESS:
    return {...state, isLoadingRepos: false, repos: action.res}
  case githubActions.FETCH_ARTICLES_ERROR400:
  case githubActions.FETCH_ARTICLES_ERROR500:
  case githubActions.FETCH_ARTICLES_FAILURE:
    return {...state, isLoadingRepos: false}
  default:
    return state
  }
}