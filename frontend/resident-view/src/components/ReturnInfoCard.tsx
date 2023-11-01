interface Props {
    title: string,
    data: string
}

export function ReturnInfoCard({title, data}: Props) {
    return (
        <div className='border border-gray-500 p-5 text-center'>
            <h2 className='text-lg font-serif'>
                {title}
            </h2>
            <p>
                {data}
            </p>
        </div>
    )
}