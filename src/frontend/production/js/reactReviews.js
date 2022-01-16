function Review(props) {

}

function ReviewsList() {
  const reviews = [{
    "professor": "Dr.T",
    "semester": "WINTER",
    "course_num": "CMPUT174",
    "overall_rate": 1,
    "difficulty": 1,
    "usefulness": 1,
    "workload": 1,
    "interest": 1,
    "comment": "123",
    "date": "2022-01-16"
  },{
    "professor": "Dr.H",
    "semester": "FALL22",
    "course_num": "CMPUT174",
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
    "course_num": "CMPUT174",
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
      {reviews.map((reviewData) => <Review data={reviewData}/>)};
    </div>
  );
}

ReactDOM.render(<ReviewsList/>, document.querySelector("div.react-root"));
