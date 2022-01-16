function Review(props) {
  return (
    <div className="review">
      <div className="metrics">
        <div className="rating">
          <p className="big-digit enlarge">{props.data.overall_rate}</p>
          <p className="small-digit">/5</p>
        </div>
        <div className="review-table">
          <p className="category minify">DIFFICULTY</p>
          <p className="big-digit minify">{props.data.difficulty}</p>

          <p className="category minify">USEFULNESS</p>
          <p className="big-digit minify">{props.data.usefulness}</p>

          <p className="category minify">WORKLOAD</p>
          <p className="big-digit minify">{props.data.workload}</p>

          <p className="category minify">INTEREST</p>
          <p className="big-digit minify">{props.data.interest}</p>
        </div>
      </div>
      <div className="details">
        <div className="section">
          <div className="consecutive-container">
            <p className="sec-title">PROFESSOR</p>
            <p className="sec-text">{props.data.professor}</p>
          </div>
          <div className="consecutive-container">
            <p className="sec-title">SECTION</p>
            <p className="sec-text">{props.data.semester}</p>
          </div>
        </div>
        <p className="review-text">{props.data.comment}</p>
        <div className="review-metadata">
          <p className="author">Submitted by delorenz</p>
          <p className="posted-date">{props.data.date}</p>
        </div>
      </div>
    </div>
  )
}

function ReviewsList() {
  const reviews = [{
    "professor": "Dr. Imanuelov",
    "semester": "WINTER22",
    "course_num": "401",
    "overall_rate": 4,
    "difficulty": 2,
    "usefulness": 5,
    "workload": 3,
    "interest": 4,
    "comment": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam amet assumenda" +
      " cumque dolorum est facere, illum, inventore ipsam itaque mollitia," +
      " officiis omnis quas qui quisquam saepe sed unde voluptate voluptatem. Lorem ipsum dolor sit amet," +
      " consectetur adipisicing elit. Aperiam consequatur consequuntur cum dignissimos eum eveniet facere in" +
      " incidunt labore natus, provident quam qui quisquam reiciendis" +
      " repellendus repudiandae rerum similique sunt voluptas. Lorem ipsum dolor sit amet, consectetur" +
      " adipisicing elit. A aliquam corporis eaque ex fuga ipsam nihil ratione sint ut voluptatem?",
    "date": "16-01-2022"
  },{
    "professor": "Dr.H",
    "semester": "FALL22",
    "course_num": "401",
    "overall_rate": 5,
    "difficulty": 3,
    "usefulness": 2,
    "workload": 2,
    "interest": 5,
    "comment": "This course was great! So glad I took it orem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate dicta doloremque ducimus earum eius\n" +
      "            eligendi enim eum eveniet hic id illum molestias nemo omnis quam qui reprehenderit ullam voluptas,\n" +
      "            voluptatibus.",
    "date": "2021-07-16"
  },{
    "professor": "Dr.R",
    "semester": "SUMMER15",
    "course_num": "401",
    "overall_rate": 3,
    "difficulty": 1,
    "usefulness": 0,
    "workload": 5,
    "interest": 5,
    "comment": "This course was great! So glad I took it orem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate dicta doloremque ducimus earum eius\n" +
      "            eligendi enim eum eveniet hic id illum molestias nemo omnis quam qui reprehenderit ullam voluptas,\n" +
      "            voluptatibus.",
    "date": "2015-01-16"
  }];
  return (
    <div className="reviews">
      <h1 className="reviews-header">REVIEWS</h1>
      {reviews.map((reviewData) => <Review data={reviewData}/>)}
    </div>
  );
}

ReactDOM.render(<ReviewsList/>, document.querySelector("div.react-root"));
