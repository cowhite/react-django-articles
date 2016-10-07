import React from "react";
import { connect } from "react-redux";

import * as articlesActions from "../actions/articlesActions";
import {Header} from "../components/Header";
import ArticlesList from "../components/ArticlesList";
export *  from "../reducers";


@connect(state => ({
  articles: state.articles
}))
export default class AppContainer extends React.Component {
  componentDidMount() {
    let {dispatch, articles} = this.props
    if (!articles.isLoadingRepos && articles.repos === undefined) {
      dispatch(articlesActions.fetchRepos())
    }
  }

  renderLoading() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            Loading...
          </div>
        </div>
      </div>
    )
  }

  render() {
    let {articles} = this.props
    if (articles.isLoadingRepos || articles.repos === undefined) {
    return this.renderLoading()
  }
    return (
      <div className="container">
        <div className="row">
          <div className ="col-xs-10 col-xs-offset-1">
            <Header/>
          </div>
        </div>
        <div className="row">
          <div className ="col-xs-10 col-xs-offset-1">
            {articles.repos !== undefined &&
              <ArticlesList repos={articles.repos} />
            }
          </div>
        </div>
      </div>
    )
  }
}