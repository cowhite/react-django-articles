import React from "react"

export default class ArticlesList extends React.Component {
  render() {
    let {repos} = this.props
    let repoNodes = []
    repos.forEach((item, index) => {
      let node = (
        <div key={item.id}>
          <h1>{item.title}</h1>
          <br/>
          <p><strong>Article:</strong>{item.content}</p>
          <p><strong>Author:</strong>{item.author_name}</p>
        </div>
      )
      repoNodes.push(node)
    })

    return (
      <div>{repoNodes}</div>
    )
  }
}